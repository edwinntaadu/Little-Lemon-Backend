#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"), 
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'), 
    path('menu-items/', views.MenuItemsViewSet.as_view({'get':'list', 'post':'create'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    #path('menu-items/', views.MenuItemsView.as_view()),
    #path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories/', views.CategoryViewSet.as_view({'get':'list', 'post':'create'})),
    path('categories/<int:pk>', views.CategoryViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('api-token-auth/', obtain_auth_token),
]
