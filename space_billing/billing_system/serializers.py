from rest_framework import serializers

from .models import Bill, BillProduct, Customer, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = BillProduct
        fields = ["product_id", "quantity"]


class BillSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    products = BillProductSerializer(many=True)
    total = serializers.IntegerField()

    class Meta:
        model = Bill
        fields = ['customer', 'products', 'total']

    def create(self, validated_data):
        customer = validated_data["customer"]
        products_data = validated_data.pop("products")
        total = 0

        bill = Bill.objects.create(customer=customer, total=total)
        for product_data in products_data:
            product = product_data["product_id"]
            quantity = product_data["quantity"]
            BillProduct.objects.create(
                customer=customer, product=product, quantity=quantity, bill=bill
            )
            total += product.price * quantity

        bill.total = total
        bill.save()

        return bill
