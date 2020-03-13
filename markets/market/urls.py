from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('add_product',views.add_product,name='add_product'),
    path('delete/<slug:productid>',views.delete_product,name='delete_product'),
]