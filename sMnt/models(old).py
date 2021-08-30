#Model definitions
from django.db import models
class Statement(models.Model):
	branch = models.CharField(max_length=20, blank=False, default='')
	customer_name = models.CharField(max_length=100, blank=False)
	acc_no = models.CharField(max_length=100, blank=False, default='')
	initial_serial_number = models.CharField(max_length=100, blank=False)
	final_serial_number = models.CharField(max_length=100, blank=False)
	date = models.DateTimeField(auto_now=True)
class Cancelled(models.Model):
	initial_serial_number =  models.CharField(max_length=100, blank=False, default='')
	final_serial_number = models.CharField(max_length=100, blank=False, default='')
	cancellation_date = models. DateTimeField(auto_now=True)
class Init(models.Model):
	initial_serial_number = models.CharField(max_length=100,blank=False)
	final_serial_number = models.CharField(max_length=100,blank=False)
	current_serial_number = models.CharField(max_length=100,blank=False)