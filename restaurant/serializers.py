#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Menu
        fields = ['id','name','price','menu_item_description','category','category_id']
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
                
        
        
        
 
#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url','username','email','groups']