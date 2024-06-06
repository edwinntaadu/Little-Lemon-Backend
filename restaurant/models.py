from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    booking_slot = models.SmallIntegerField()

    def __str__(self): 
        return self.name


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    
    def __str__(self):
        return self.title
 
    
class Menu(models.Model):
   name = models.CharField(max_length=255) 
   price = price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')
   category = models.ForeignKey(Category, on_delete=models.PROTECT)

   def __str__(self):
        return self.name


