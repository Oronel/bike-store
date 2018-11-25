from django.shortcuts import render
from first_app.models import Customer, Vehicle, VehicleType, VehicleSize, RentalRate, Rental
from first_app import forms
# Create your views here.

def menu(request):
	return render(request, 'menu.html')

def rentals(request):
	rentals = Rental.objects.all()
	return render(request, 'rentals.html', {'rentals': rentals})

def customers(request):
	customers = Customer.objects.all()
	return render(request, 'customers.html', {'customers': customers})

def customer(request,customer_id):
	custo = Customer.objects.filter(id=customer_id)
	return render(request, 'custo.html', {'customer': custo})

def rent(request, rental_id):
	rent = Rental.objects.filter(id=rental_id)
	return render(request, 'rent.html', {'rental': rent})

def add_customer_form(request):
	form = forms.new_customer_form()
	if request.method == 'POST':
		form = forms.new_customer_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return menu(request)
		else:
			print('Error - form is invalid')
	return render(request, 'add_custo_form.html', { 'form' : form })

def add_rental_form(request):
	form = forms.new_rental_form()
	if request.method == 'POST':
		form = forms.new_rental_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return menu(request)
		else:
			print('Error - form in invalid')
	return render(request, 'add_rental_form.html', { 'form' : form })

def add_vehicle_form(request):
	form = forms.new_vehicle_form()
	if request.method == 'POST':
		form = forms.new_vehicle_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return menu(request)
		else:
			print('Error - form in invalid')
	return render(request, 'add_vehicle_form.html', { 'form' : form })

