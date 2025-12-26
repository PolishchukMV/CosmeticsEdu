from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category


def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all()[:4]  # 4 рекомендуемых продукта
    return render(request, 'shop/home.html', {'categories': categories, 'featured_products': featured_products})


def about(request):
    return render(request, 'shop/about.html')


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def contacts(request):
    return render(request, 'shop/contacts.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'shop/profile.html')

def sitemap(request):
    return render(request, 'shop/sitemap.html')