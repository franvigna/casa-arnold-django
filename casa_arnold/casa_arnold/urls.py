from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('product/<int:id>/', views.product, name='product'),
    path('category/<str:categories>/', views.category, name='category'),
    path('allproducts/', views.allproducts , name="allproducts"),
]
