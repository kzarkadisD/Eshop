from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from django.db.models import Q

def home(request):
    # Your view logic here
    return render(request, 'app1/shop.html')  # You should return an HTTP response


def about(request):
    return render(request, 'app1/about.html')

class ProductListView(ListView):
    model = Product
    template_name = 'app1/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context


def product_search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, 'app1/search.html', {'products': products, 'categories': categories, 'subcategories': subcategories})


