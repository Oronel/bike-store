from django import forms
from django.core import validators
from first_app.models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate

class new_customer_form(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class new_rental_form(forms.ModelForm):
	class Meta:
		model = Rental
		fields = ['customer', 'vehicle']

class new_vehicle_form(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'