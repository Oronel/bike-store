from django.db import models
from datetime import datetime
# Create your models here.


class Customer(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField(max_length=264, unique=True)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=264)
	city = models.CharField(max_length=264)
	country = models.CharField(max_length=264)

	def __str__(self):
		return self.first_name


class VehicleType(models.Model):
	name = models.CharField(max_length=264)

	def __str__(self):
		return self.name


class VehicleSize(models.Model):
	name = models.CharField(max_length=264)

	def __str__(self):
		return self.name


class Vehicle(models.Model):
	vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
	date_created = models.DateField()
	real_cost = models.IntegerField()
	size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

	def __str__(self):
		return self.vehicle_type.name


class Rental(models.Model):
	rental_date = models.DateField(default=datetime.now())
	return_date = models.DateField(null=True, blank=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

	def __str__(self):
		return self.rental_date

class RentalRate(models.Model):
	daily_rate = models.IntegerField()
	vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
	vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

	def __str__(self):
		return self.daily_rate