from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def filter_attr(hardware):
	if hardware['hardware_type'] == 'Server' :
		del hardware['windows_up_to_date']
		del hardware['ms_office_up_to_date']
		del hardware['pc_name']
		del hardware['keyboard_serial_number']
		del hardware['mouse_serial_number']
		del hardware['printer_serial_number']
		del hardware['monitor_serial_number']
		del hardware['system_unit_serial_number']
	elif hardware['hardware_type'] == 'Desktop' :
		pass
	else :
		del hardware['windows_up_to_date']
		del hardware['ms_office_up_to_date']
		del hardware['pc_name']
		del hardware['antivirus_up_to_date']
		del hardware['operating_system']
		del hardware['keyboard_serial_number']
		del hardware['mouse_serial_number']
		del hardware['printer_serial_number']
		del hardware['monitor_serial_number']
		del hardware['system_unit_serial_number']