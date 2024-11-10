from django.contrib import admin
from .models import Profile, DriverDetails, CustomerDetails, Trip

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at', 'updated_at')
    search_fields = ('user__username', 'role')

@admin.register(DriverDetails)
class DriverDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'vehicle_type', 'vehicle_plate', 'rating', 'availability')
    search_fields = ('user__username', 'vehicle_type', 'license_number')
    list_filter = ('availability',)

@admin.register(CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'payment_method')
    search_fields = ('user__username', 'phone_number')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('customer', 'driver', 'start_location', 'end_location', 'status', 'trip_time', 'cost')
    search_fields = ('customer__user__username', 'driver__user__username', 'start_location', 'end_location')
    list_filter = ('status', 'trip_time')
