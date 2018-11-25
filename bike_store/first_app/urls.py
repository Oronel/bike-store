from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/rental/', views.rentals, name='rentals'),
    path('menu/customers/', views.customers, name='customers'),
    path('menu/customers/<int:customer_id>/', views.customer, name='customer'),
    path('menu/rental/<int:rental_id>/', views.rent, name='rental'),
    path('menu/addcusto/', views.add_customer_form, name = 'form_custo'),
    path('menu/addrent/', views.add_rental_form, name = 'form_rent'),
    path('menu/addvehicle/', views.add_vehicle_form, name = 'form_vehicle'),
 ]