from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, SellProductForm
from datetime import date
from django.db.models import Sum

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def update_selling_price(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = SellProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SellProductForm(instance=product)
    return render(request, 'shop/update_selling_price.html', {'form': form, 'product': product})

def dashboard(request):
    products = Product.objects.all()
    total_sales = products.aggregate(Sum('selling_price'))['selling_price__sum'] or 0
    today_profit = sum((p.selling_price - p.buy_price) for p in products if p.selling_price)

    return render(request, 'shop/dashboard.html', {
        'products': products,
        'total_sales': total_sales,
        'today_profit': today_profit,
    })