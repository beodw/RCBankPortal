from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def get_usage(a,b):
	return ( int(a) - int(b) )

