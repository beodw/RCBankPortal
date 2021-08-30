from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def rm_und(value):
	return value.replace('_', ' ')

