from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
    path("customers/", views.CustomerList.as_view(), name="customer-list"),
    path("customers/<int:pk>/", views.CustomerDetail.as_view(), name="customer-detail"),
    path("bills/", views.BillListCreate.as_view(), name="bill-list"),
    path("bills/<int:pk>/", views.BillDetail.as_view(), name="bill-detail"),
]
