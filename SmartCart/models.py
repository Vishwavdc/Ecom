from django.db import models

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    Book_Title = models.CharField(max_length=200)
    Book_Author = models.CharField(max_length=100)
    Year_Of_Publication = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    Image_URL_S = models.URLField()
    Image_URL_M = models.URLField()
    Image_URL_L = models.URLField()

    def __str__(self):
        return self.Book_Title

class Rating(models.Model):
    User_ID = models.IntegerField()
    ISBN = models.CharField(max_length=13)
    Book_Rating = models.IntegerField()
    # Add other fields

    class Meta:
        unique_together = ['User_ID', 'ISBN']

    def __str__(self):
        return f'Rating {self.Book_Rating} for ISBN {self.ISBN}'


class User(models.Model):
    User_ID = models.IntegerField(unique=True)
    Location = models.CharField(max_length=100)
    Age = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'User {self.User_ID} from {self.Location}'

from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='CartItem')

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='OrderItem')
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='Pending')

class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
