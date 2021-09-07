from django.shortcuts import render,redirect
from blog.forms import *
from django.contrib import messages
# Create your views here.
def base(response):
    return render(response, 'blog/base.html')
def home(response):
    
    return render(response, 'blog/home.html')

def services(response):
    products = Product.objects.filter(available=True)
    context = {'products':products}
    
    return render(response, 'blog/services.html',context)

def service_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}

    return render(request, 'blog/service_detail.html',context)

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request,"Welcome")
        return redirect('add_product')
        #elif:
           # messages.success(request,"product not uploaded, try again")
            #return redirect('add_product')
    else:
       
        form = ProductForm()

    context = {'form':form}
    return render(request, 'blog/add_product.html',context)
