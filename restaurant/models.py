from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    booking_slot = models.SmallIntegerField()

    def __str__(self): 
        return self.name
    
class Menu(models.Model):
   name = models.CharField(max_length=255) 
   price = price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
        return self.name