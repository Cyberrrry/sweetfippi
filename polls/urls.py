from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:myid>', views.Productview, name='product'),
    path('address/<int:myid>', views.address, name='address'),
    path('payselect/<int:myid>', views.payselect, name='payselect'),
    path('order/<int:myid>', views.order, name='order'),
    path('payment/<int:myid>', views.payment, name='payment'),
]
