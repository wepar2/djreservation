from django.contrib import admin
from .models import MyObject

# Register your models here.

class myobjectAdmin(admin.ModelAdmin):

	list_display = ['name','quantity', 'measurement_unit']


admin.site.register(MyObject, myobjectAdmin)
