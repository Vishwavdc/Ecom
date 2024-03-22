from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # New URL pattern for the home page
    path('book_list/', views.book_list, name='book_list'),
    path('search/', views.search, name='search'),
    path('book/<str:isbn>/', views.book_detail, name='book_detail'),
    path('add_to_cart/<str:isbn>/', views.add_to_cart, name='add_to_cart'),
    # View Cart
    path('cart/', views.cart_view, name='cart_view'),
    # Place Order
    path('place_order/', views.place_order, name='place_order'),
]
