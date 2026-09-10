from django.shortcuts import render, redirect
from .models import Category, Product, Customer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'object_list': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category_detail.html', {'object': category})

def category_create(request):
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('category_list')
    return render(request, 'form.html')

def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('category_list')
    return render(request, 'form.html', {'object': category})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'confirm_delete.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'object_list': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'object': product})

def product_create(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity')
        )
        return redirect('product_list')
    return render(request, 'form.html')

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect('product_list')
    return render(request, 'form.html', {'object': product})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'confirm_delete.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'object_list': customers})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'customer_detail.html', {'object': customer})

def customer_create(request):
    if request.method == 'POST':
        Customer.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address')
        )
        return redirect('customer_list')
    return render(request, 'form.html')

def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('phone')
        customer.address = request.POST.get('address')
        customer.save()
        return redirect('customer_list')
    return render(request, 'form.html', {'object': customer})

def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'confirm_delete.html')
