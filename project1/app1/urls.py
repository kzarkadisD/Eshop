from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),  # Home page (shop.html)
    path('about/', views.about, name='about'),  # About page
    path('shop/', views.ProductListView.as_view(), name='product_list'),  # Shop page
    path('search/', views.product_search, name='product_search'),  # Search page
    path('', views.home, name='home'),  # Define a URL pattern for the 'home' view
    # Other URL patterns
]
