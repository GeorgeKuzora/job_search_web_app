from django.contrib import admin

from .models import Address, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Address)
