import uuid

from django.db import models

# Create your models here.


# CLASS product
    # product_name
    # product_category
    # product_image
    # procut_price
    # product_rating

# CLASS category
    # title
    # product = ForeignKey
# ClASS product_category
    # title
    # product = ForeignKey

# CLASS MESSAGE
    # name
    # phone_number
    # email
    # product
    #message


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=False, upload_to='product', default='empty.png')
    price = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2)
    rating = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        return f'{self.title}'


class Message(models.Model):
    name = models.CharField(blank=True, null=False, max_length=50)
    phone_number = models.IntegerField(blank=True, null=False)
    email = models.EmailField(blank=True, null=False, max_length=254)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=500, blank=True, null=True)

class About(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    about = models.TextField(max_length=500, blank=True, null=False)
    image = models.ImageField(blank=True, null=False, upload_to='site', default='empty.png')
    socials_inst = models.URLField(blank=True, null=True)
    socials_twitter = models.URLField(blank=True, null=True)
    socials_facebook = models.URLField(blank=True, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
