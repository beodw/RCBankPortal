#Gen ('value','label') for fields that require select
def gen_choices(query_set, attr, field_name):
	choices = [(getattr(obj, attr), getattr(obj, attr)) for obj in query_set]
	choices.insert(0 , ('','--Choose '+field_name+'--') ) #Prepend default message
	return choices

from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Branch
 
#Get all branches, i.e. non-admin or non-superuser users, from django.auth.user table.
# branches = get_user_model().objects.filter(  Q(is_superuser=0) & Q(is_staff=0) & ~Q(username='Admin') )
branches = Branch.objects.filter(is_active=True)
#Gen branch choices
branches = gen_choices(query_set=branches, attr='name', field_name='Branch')
#Yes/No choices
yesno = [('','--Choose--'), ('True', 'Yes'), ('False', 'No')]

# Hardware.objects.filter(type=)
hardware_types = [('', '--Choose Type--'), ('Server','Server'), ('SystemUnit', 'Work Station'), ('Other','Other')]


from .models import *
from django import forms

# Function to create input attrs.
def gen_attrs(attrs={}, to_append={}, to_remove=[]):
	attrs.update({'class' :'form-control mb-1', 'required':'', 'style':'background:white;'})
	if bool(to_append):
		attrs.update(to_append)
	if bool(to_remove):
		for key in to_remove:
			attrs.pop(key)
	return attrs

class Select_branch(forms.ModelForm):
	class Meta:
		model = Supply
		fields = ['branch']
		widgets = {  'branch' : forms.Select( attrs=gen_attrs( ), choices=branches ) }

class Department_form(forms.Form):
	department = forms.CharField(   widget=forms.Select( attrs=gen_attrs( to_append={'class': 'ui dropdown mb-1 form-control'} ) ), label='Department or location')


class Supply_hardware_form(forms.ModelForm):
	class Meta:
		model = Supply
		exclude = ['status']
		widgets = {
			#'department': forms.Select(attrs=gen_attrs() ), #choices are set in views.py before rendering page.
			'branch': forms.Select(attrs=gen_attrs( ), choices=branches),

			'assigned_to':  forms.TextInput(  attrs=gen_attrs(  {'placeholder' : 'e.g. The Director of Business Center'}  )  ),

			'date_of_supply': forms.DateInput(attrs=gen_attrs( to_append={'type':'date' }), ),
			'date_of_confirmation': forms.DateInput(attrs=gen_attrs( {'type':'date'}  )   ),

		}
		
class Add_hardware_form(forms.ModelForm):
	class Meta:
		model = Hardware
		exclude = ['branch','is_replaced', 'condition', 'is_received', 'supply','hardware_type', 'assigned_to', 'department','date_of_supply']
		widgets = {
			'serial_number' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. CXQL12R' }) ),
			'brand_and_model' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Dell OptiPlex 3080'}) ),
	
			# 'hardware_type': forms.Select(attrs=gen_attrs(), choices=hardware_types),

			#'department': forms.Select(attrs=gen_attrs(), choices=(
			#		('CURRENT ACCOUNTS','CURRENT ACCOUTNS'), ('SAVINGS ACCOUTNS', 'SAVINGS ACCOUTNS'), ('RISK DEPARTMENT','RISK DEPARTMENT'), ('ENTRIES','ENTRIES'), ('TREASURY','TREASURY'), ('FINANCE DEPARTMENT','FINANCE DEPARTMENT'), ('COMPUTER CENTER', 'COMPUTER CENTER')
			#	)
			#	)
			
		}

class Software_capable_hardware_form_components(forms.ModelForm):
	class Meta:
		model = Software_capable_hardware
		exclude = ['is_replaced', 'condition','branch', 'assigned_to', 'hardware_type', 'date_of_supply', 'serial_number', 'brand_and_model', 'department', 'is_received', 'supply']
		widgets = {
			'operating_system' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Windows Server 2012 r2', 'value':'Windows Server 2012 r2'}) ),

			'antivirus_up_to_date': forms.Select(attrs=gen_attrs(), choices=yesno),
			'operating_system_up_to_date': forms.Select(attrs=gen_attrs(), choices=yesno),
		}

class System_unit_form_components(forms.ModelForm):
	class Meta:
		model = System_unit
		exclude = ['is_replaced', 'condition','branch', 'assigned_to', 'hardware_type', 'date_of_supply', 'serial_number', 'brand_and_model', 'department', 'is_received', 'supply', 'department']
		fields = [
				  'system_unit_name',

				  'service_tag_code',

				  'monitor_serial_number',
				  'keyboard_serial_number',
				  'mouse_serial_number',

				  'operating_system',

				  'operating_system_up_to_date',
				  'ms_office_up_to_date',

				  'antivirus_up_to_date',

				  'printer_brand_and_model', 
				  'printer_serial_number',

				  'scanner_brand_and_model',
				  'scanner_serial_number',

				  'modem_brand_and_model',
				  'modem_serial_number',
				  ]
		widgets = {
			'antivirus_up_to_date': forms.Select(attrs=gen_attrs(), choices=yesno),
			'operating_system_up_to_date' : forms.Select(attrs=gen_attrs(), choices=yesno),

			'operating_system' : forms.TextInput(attrs=gen_attrs( {'placeholder': 'e.g. Windows 10 Pro'} )),

			'ms_office_up_to_date' : forms.Select(attrs=gen_attrs(), choices=yesno),


			'system_unit_name' : forms.TextInput(attrs=gen_attrs( {'placeholder': 'e.g. FCX-MGR-01'}) ),
			'service_tag_code' : forms.TextInput(attrs=gen_attrs(to_remove=['required','type']) ),

			'monitor_serial_number': forms.TextInput(attrs=gen_attrs(to_remove=['required'])),
			'keyboard_serial_number': forms.TextInput(attrs=gen_attrs(to_remove=['required'])),
			'mouse_serial_number' : forms.TextInput(attrs=gen_attrs(to_remove=['required'])),

			'printer_brand_and_model' : forms.TextInput(attrs=gen_attrs(attrs={'placeholder':'e.g. HP LaserJet 86'}, to_remove=['required'])),
			'printer_serial_number' : forms.TextInput(attrs=gen_attrs(to_remove=['required'])),

			'scanner_brand_and_model' : forms.TextInput(attrs=gen_attrs(attrs={'placeholder':'e.g. HP ScanJet Pro 2500 f1'}, to_remove=['required'])),
			'scanner_serial_number' : forms.TextInput(attrs=gen_attrs(to_remove=['required'])),


			'modem_brand_and_model' : forms.TextInput(attrs=gen_attrs(attrs={'placeholder':'e.g. D-Link'}, to_remove=['required'])),
			'modem_serial_number' : forms.TextInput(attrs=gen_attrs(to_remove=['required'])),

		}

class Other(forms.Form):
	_type = forms.ChoiceField(choices=[('Printer','Printer'),('Scanner','Scanner'),('Tablet','Tablet'),('Mouse','Mouse'),('Keyboard','Keyboard'),('Monitor','Monitor'),('Router','Router'),('Switch','Switch')],widget=forms.Select(attrs=gen_attrs({'class':'form-control','required':'','placeholder':'e.g. Mouse, Scanner'})))
	# _type = forms.CharField(label='Type', widget=forms.TextInput(attrs=gen_attrs( {'class' :'form-control', 'required':'', 'placeholder':'e.g. Laptop, Tablet'})) )


class Update_generic_hardware_form(forms.ModelForm):
	class Meta:
		model = Hardware
		exclude = ['is_replaced', 'condition', 'is_received', 'supply', 'date_of_supply']
		widgets = {
			'assigned_to' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Glena McCarthy'}) ),
			'serial_number' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. CXQL12R', 'minlength':'5'}) ),
			'brand_and_model' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Dell OptiPlex 3080'}) ),
			# 'date_of_supply' : forms.DateInput(attrs=gen_attrs( {'type':'date'}) ),
			# 'branch': forms.TextInput(attrs=gen_attrs()),
			'hardware_type': forms.TextInput(attrs={'class' :'form-control', 'required':'', 'style':'background:white;'} ),
			'department' : forms.TextInput(attrs=gen_attrs({'placeholder' : 'e.g. Finance Department', 'readonly':''}, to_remove=['required'])),
		}

class Replace_hardware_form(forms.ModelForm):
	class Meta:
		model = Hardware
		exclude = ['is_replaced', 'condition', 'is_received','supply', 'department']
		widgets = {
			'assigned_to' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Accounting assigned_to'}) ),
			'serial_number' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. CXQL12R', 'minlength':'5'}) ),
			'brand_and_model' : forms.TextInput(attrs=gen_attrs( {'placeholder':'e.g. Dell OptiPlex 3080'}) ),
			'date_of_supply' : forms.DateInput(attrs=gen_attrs( {'type':'date'}) ),

			'branch': forms.Select(attrs={'class' :'form-control', 'required':'', 'style':'background:white; '}, choices=branches),
			'hardware_type': forms.TextInput(attrs=gen_attrs(),),
			# 'department' : forms.TextInput(attrs=gen_attrs({'placeholder' : 'e.g. Finance Department'}, to_remove=['required'])),
		}

class Add_branch_form(forms.Form):
	branch_name = forms.CharField(widget=forms.TextInput(attrs=gen_attrs({'placeholder':'e.g. FWILK'})),min_length=2, strip=True) 
	branch_password = forms.CharField(widget=forms.TextInput(attrs=gen_attrs({'placeholder':'Password must be at least 8 characters long', 'type':'password'})),min_length=8, strip=True)
	verify_password = forms.CharField(widget=forms.TextInput(attrs=gen_attrs({'placeholder':'Re-enter password', 'type':'password'})),min_length=8, strip=True)
	admin_password = forms.CharField(widget=forms.TextInput(attrs=gen_attrs({'type':'password'})),min_length=8, strip=True)


# Forms for admin
class Report_form(forms.Form):
	generate_report_branch_options = list ( branches ) #Create new list, because django passes values by reference.
	generate_report_branch_options.insert(1, ('All Branches', 'All Branches')) #insert All Branches option.
	generate_for = forms.ChoiceField( widget=forms.Select(attrs=gen_attrs({'class':'ui fluid search dropdown'})), choices=generate_report_branch_options )
	# from_date = forms.DateField(  widget=forms.TextInput(   attrs=gen_attrs(to_append={'type':'date'}) ), label='From'   ) 
	# to_date = forms.DateField(  widget=forms.TextInput(   attrs=gen_attrs(to_append={'type':'date'}) ), label='To'   ) 
