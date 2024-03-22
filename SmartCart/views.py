from django.shortcuts import render
from .models import Book,Rating
from django.core.paginator import Paginator
from django.db.models import Avg,Count
# Create your views here.


def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 40)  # Show 40 books per page
    page = request.GET.get('page')
    books = paginator.get_page(page)
    rows = [books[i:i + 4] for i in range(0, len(books), 4)]  # Divide books into rows
    return render(request, 'book_list.html', {'rows': rows, 'books': books})

def book_detail(request, isbn):
    book = Book.objects.get(ISBN=isbn)
    avg_data = Rating.objects.filter(ISBN=isbn).aggregate(avg_rating=Avg('Book_Rating'), total_ratings=Count('Book_Rating'))
    average_rating = avg_data['avg_rating']
    total_ratings = avg_data['total_ratings']
    return render(request, 'book_detail.html', {'book': book, 'average_rating': average_rating, 'total_ratings': total_ratings})

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL query parameters (default to an empty string)
    print(f"Received query: {query}")
    if query:
        # Perform a search query on the Book model using a case-insensitive filter
        results = Book.objects.filter(Book_Title__icontains=query)
    else:
        results = []  # No results if the query is empty

    return render(request, 'search.html', {'query': query, 'results': results})

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Cart, CartItem, Book

def add_to_cart(request, isbn):
    # Get the user
    user = request.user

    # Get the book to add to the cart
    book = Book.objects.get(ISBN=isbn)

    # Check if the user already has a cart
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = Cart(user=user)
        cart.save()

    # Check if the book is already in the cart
    try:
        cart_item = CartItem.objects.get(cart=cart, book=book)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem(cart=cart, book=book, quantity=1)
        cart_item.save()

    return redirect('cart_view')

def cart_view(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = cart.cartitem_set.all()  # Retrieve cart items

    return render(request, 'cart.html', {'cart_items': cart_items})

def place_order(request):
    user = request.user
    cart = Cart.objects.get(user=user)

    # Create an order
    order = Order(user=user)
    order.save()

    # Move items from the cart to the order
    for cart_item in cart.cartitem_set.all():
        order_item = OrderItem(book=cart_item.book, order=order, quantity=cart_item.quantity)
        order_item.save()
        cart_item.delete()

    return redirect('order_view', order.id)
