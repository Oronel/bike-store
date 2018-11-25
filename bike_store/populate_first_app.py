import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import django
django.setup()




# fake populate script
from datetime import datetime
import random
from faker import Faker
from first_app.models import Customer, Vehicle, Rental, RentalRate, VehicleType, VehicleSize

fakegen = Faker()

type_list = ['bike', 'electric bike', 'scooter']
size_list = ['small', 'medium', 'large', 'double']


def add_type():
	for t in type_list:
		typ = VehicleType.objects.get_or_create(name= t)[0]
		typ.save()
	return typ

def add_size():
	for s in size_list:
		size = VehicleSize.objects.get_or_create(name= s)[0]
		size.save()
	return size

def populate_customer(N=5):

	for entry in range(N):
		# get topic for the entry
		fake_first_name = fakegen.first_name()
		fake_last_name = fakegen.last_name()
		fake_email = fakegen.email()
		fake_phone_number = fakegen.phone_number()
		fake_address = fakegen.street_address()
		fake_city = fakegen.city()
		fake_country = fakegen.country()

		customer = Customer.objects.get_or_create(first_name= fake_first_name, last_name=fake_last_name, email=fake_email, phone_number=fake_phone_number, address=fake_address, city=fake_city, country=fake_country)[0]

	return customer

def populate_vehicle(N=5):

	size = add_size()
	typ = add_type()

	for entry in range(N):
		fake_real_cost = fakegen.pyint()
		fake_date_created = fakegen.date()

		vehicle = Vehicle.objects.get_or_create(vehicle_type= typ, date_created= fake_date_created, real_cost= fake_real_cost, size= size)[0]
	return vehicle

def populate_rental(N=5):
	for entry in range(N):

		rental_fake_rental_date = fakegen.date_time_between(start_date='-1y', end_date='-7d',tzinfo=None)
		rental_fake_return_date = fakegen.date_time_between_dates(datetime_start=rental_fake_rental_date, datetime_end=datetime.now(), tzinfo=None)
		rental_fake_customer = populate_customer()
		rental_fake_vehicule = populate_vehicle()



		rental = Rental.objects.get_or_create(rental_date=rental_fake_rental_date, return_date=rental_fake_return_date,
			customer= rental_fake_customer, vehicle= rental_fake_vehicule)[0]

def populate_rentalRate():

	vehicules_type = VehicleType.objects.all()
	vehicules_size = VehicleSize.objects.all()

	for element in vehicules_type:
		for size in vehicules_size:
			if element.name == 'bike':
				fake_vehicule_daily_rate = 25.00
			elif element.name == 'electric bike':
				fake_vehicule_daily_rate = 100.00
			elif element.name == 'scooter':
				fake_vehicule_daily_rate = 180.00

			rental_rate = RentalRate.objects.get_or_create(daily_rate=fake_vehicule_daily_rate, vehicle_type=element, vehicle_size=size)[0]


if __name__ == '__main__':
	print('Starting to populate...')
	# populate_vehicle(20)
	# populate_customer(25)
	# populate_rental(15)
	populate_rentalRate()
	print('finished populating!')








