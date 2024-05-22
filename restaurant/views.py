from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def home(request): 
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

#class UserViewSet(viewsets.ModelViewSet):
#   permission_classes = [IsAuthenticated]
#   queryset = User.objects.all()
#   serializer_class = UserSerializer