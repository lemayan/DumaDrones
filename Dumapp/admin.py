from django.contrib import admin

# Register your models here.

from Dumapp.models import Member, Contact

admin.site.register(Member)
admin.site.register(Contact)