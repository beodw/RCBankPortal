from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Statement)
admin.site.register(Cancelled)
admin.site.register(Init)
admin.site.register(Quant)
