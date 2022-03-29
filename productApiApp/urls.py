from django.urls import path

from .views import ProductView, ProductUpdate


urlpatterns = [
    path('product/', ProductView.as_view()),
    path('update-product/<int:product_pk>', ProductUpdate.as_view()),
]
