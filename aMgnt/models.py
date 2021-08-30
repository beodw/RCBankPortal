#Model definitions
#If your looking for a branches table they are implemented using django.contrib.auth. Check forms.py for details.
from django.db import models
import math
# from django.contrib.auth
class Branch(models.Model):
	name = models.CharField(max_length=100, blank=False, default='')
	password = models.CharField(max_length=100, blank=False, default='')
	is_active = models.BooleanField(default=True, blank=True)

class Department(models.Model):
	branch =  models.CharField(max_length=100, blank=False, default='')
	name = models.CharField(max_length=100, blank=False)

class Supply(models.Model):
	branch = models.CharField(max_length=100, blank=False) #Django auth is used to implement branch names.
	date_of_confirmation = models.DateField(null=True, default=None)
	date_of_supply = models.DateField() # The date when a supplied is made. Genreated by backend. Do not give users a front end input
	status = models.CharField(max_length=100, default='Pending') # A field to indicate if a supply is received with no issue. 
													   # Pending indicates confirmation still in progess. 
													   # Received indicates acknowledgement of receipt and all hardware is correct.
													   # Problem indicates an issue found in one or more delivered hardware.
													   # System Init indicates the hardware added to the system when integrated.
	assigned_to =  models.CharField(default='', max_length=100, blank=True)
# Table to link supply to departments. So for any suppliy a list of supplied departments can  be easily generated.
# class Supplied_departments(models.Model):
# 	department = models.CharField(max_length=100, default='', blank=True)
# 	supply = models.ForeignKey(Supply, on_delete=models.PROTECT)
# Hardware table contains fileds common to all hardware accross company.
class Hardware(models.Model):		
	supply = models.ForeignKey(Supply, on_delete=models.PROTECT) # The supply the hardware belongs to.
	branch = models.CharField(max_length=200, blank=True,default='')
	hardware_type = models.CharField(max_length=11, blank=False) #make sure to limit input form to 15 char.
	brand_and_model = models.CharField(max_length=100, blank=False)
	serial_number = models.CharField(max_length=100, unique=False, blank=True, default='') # set to a special value for desktop
	condition = models.CharField(max_length=4, default='Good', blank=True) #can be Good, Bad or Mid. Generated based on the correspnding incidents for the hardware.

	is_replaced =  models.BooleanField(default=False, blank=True) #Efficient way of knowing if a hardware has been replaced. Better than looking through replacements table for each hardware.
	is_received = models.BooleanField(default=False, blank=True) # A field to represent whether a branch has acknowldge receipt of a particular hardware component.
	department = models.CharField(default='Not yet assigned', max_length=100, blank=True)
	assigned_to = models.CharField(default='Not yet assigned', max_length=100, blank=True)
	date_of_supply = models.CharField(default='', blank=True, max_length=100)
	num_rows = None
	def clean(self):
		del self.id, self.branch, self._state, self.is_received
		self.__dict__['is_replaced'] = 'Yes' if self.__dict__['is_replaced'] is True else 'No'
		self.num_rows = math.ceil(len(self.__dict__)/5)
class Software_capable_hardware(Hardware): #Hardware components that can run software i.e. Servers, laptops and maybe tablets in the future.
	antivirus_up_to_date = models.BooleanField(blank=False)
	operating_system = models.CharField(max_length=100, blank=False)
	operating_system_up_to_date = models.BooleanField(blank=False)
	def clean(self):
		del self.__dict__['hardware_ptr_id']
		self.__dict__['antivirus_up_to_date'] = 'Yes' if self.__dict__['antivirus_up_to_date'] is True else 'No'
		self.__dict__['operating_system_up_to_date'] = 'Yes' if self.__dict__['operating_system_up_to_date'] is True else 'No'
		super().clean()
class System_unit(Software_capable_hardware): #For fields specific to system units.
	system_unit_name = models.CharField(max_length=100, blank=False)
	ms_office_up_to_date = models.BooleanField(blank=False)
	service_tag_code = models.CharField(max_length=100, blank=True, default='')

	monitor_serial_number = models.CharField(max_length=100, blank=True, default='')
	keyboard_serial_number = models.CharField(max_length=100, blank=True, default='')
	mouse_serial_number = models.CharField(max_length=100, blank=True, default='')

	printer_brand_and_model = models.CharField(max_length=100, blank=True, default='')
	printer_serial_number = models.CharField(max_length=100, blank=True, default='')

	scanner_brand_and_model = models.CharField(max_length=100, blank=True, default='')
	scanner_serial_number = models.CharField(max_length=100, blank=True, default='')

	modem_brand_and_model = models.CharField(max_length=100, blank=True, default='') 
	modem_serial_number = models.CharField(max_length=100, blank=True, default='')
	def clean(self):
		super().clean()
class Incident(models.Model):
	hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
	date_of_incident = models.DateField()
	is_severe = models.BooleanField(blank=False)
	description = models.TextField(blank=False)
	status = models.CharField(max_length=12, blank=True, null=False, default='Not Resolved') #Whether or not the incident has been resolved.
	date_of_resolution = models.DateField(null=True)
	steps_taken_to_resolve = models.CharField(max_length=1000, blank=False)
class Replacement(models.Model):
	old_hardware = models.OneToOneField(Hardware, on_delete=models.PROTECT, related_name='from_old_hardware_field') #id of replaced hardware
	new_hardware = models.OneToOneField(Hardware, on_delete=models.PROTECT, related_name='from_new_field') #id of supplanting hardware
	date_of_replacement = models.DateField()
class GeneralIncident(models.Model):
	branch = models.CharField(max_length=100,blank=False)
	date = models.DateTimeField() 
	description = models.CharField(max_length=100,blank=False)
	reportingStaffName = models.CharField(max_length=100,blank=False)
	resolution = models.CharField(max_length=100,blank=True,default='')
	#resolved is an integer of the set {0,1,2} with 0 representing a new incident,
	#1 representing a resolved incident,
	#2 an incident that has been passed to a superior. 
	resolved = models.IntegerField(default=0,blank=False)
	severity = models.BooleanField(blank=False,default=False)
	def get_severity(self):
		if self.severity:
			return 'Severe'
		else:
			return 'Non-severe'
	def get_status(self):
		if self.resolved is 0:
			return 'Not Resolved'
		elif self.resolved is 1:
			return 'Resolved'
		else:
			return 'Forwarded To Supervisor'
