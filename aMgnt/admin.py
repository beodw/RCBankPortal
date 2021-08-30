from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Hardware)
admin.site.register(Software_capable_hardware)
admin.site.register(System_unit)
admin.site.register(Incident)
admin.site.register(Replacement)
admin.site.register(Branch)
admin.site.register(GeneralIncident)