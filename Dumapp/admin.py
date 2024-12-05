from django.contrib import admin

# Register your models here.

from Dumapp.models import ImageModel, Member, Contact

admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(ImageModel)