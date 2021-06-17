from django.contrib import admin
from .models import Reservation, Price, Order
"""
registering created models in admin menu
"""
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Price)
admin.site.register(Order)
