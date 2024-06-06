from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .forms import BookingForm
from .models import Menu, Booking, Category
from .serializers import MenuSerializer, BookingSerializer,CategorySerializer

# Create your views here.
def home(request): 
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            booking_slot=data['booking_slot']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                no_of_guests=data['no_of_guests'],
                booking_date=data['booking_date'],
                booking_slot=data['booking_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())
    
    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')




class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
#class MenuItemsView(generics.ListCreateAPIView):
#    queryset = Menu.objects.all()
#    serializer_class = MenuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

#class UserViewSet(viewsets.ModelViewSet):
#   permission_classes = [IsAuthenticated]
#   queryset = User.objects.all()
#   serializer_class = UserSerializer