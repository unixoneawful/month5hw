from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('api/v1/', include('product.urls') ),
    path('api/v1/users/', include('users.urls'))
]