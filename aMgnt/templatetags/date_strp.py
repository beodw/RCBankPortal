from django import template
from django.template.defaultfilters import stringfilter
import datetime
register = template.Library()

@register.filter
@stringfilter
def date_strp(date_string):
	date = datetime.datetime.strptime(date_string,'%Y-%m-%d')
	return date.strftime('%b. %d, %Y')

