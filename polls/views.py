from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Upi
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'polls/index.html', {'products': products})


def Productview(request, myid):
    products = Product.objects.filter(id=myid)
    return render(request, 'polls/product.html', {'products': products[0]})


def address(request, myid):
    products = Product.objects.filter(id=myid)
    return render(request, 'polls/address.html', {'products': products[0]})


def payselect(request, myid):
    products = Product.objects.filter(id=myid)
    return render(request, 'polls/payselect.html', {'products': products[0]})


def order(request, myid):
    products = Product.objects.filter(id=myid)
    return render(request, 'polls/order.html', {'products': products[0]})


def payment(request, myid):
    products = Product.objects.filter(id=myid)
    upi_obj = Upi.objects.all()

    context = {
        'products': products[0],
        'upi': upi_obj,
    }
    return render(request, 'polls/payment.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('table')
        else:
            messages.error(
                request, 'Invalid credinceals')
            return redirect('login')
    else:
        return render(request, 'polls/login.html')
