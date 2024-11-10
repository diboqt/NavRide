from django.db import models
from django.contrib.auth.models import User

# Enum choices
ROLE_CHOICES = [
    ('driver', 'Driver'),
    ('customer', 'Customer'),
]

TRIP_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
]

# Profile model with a role field
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# Driver Details model
class DriverDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="driver_profile")
    license_number = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)
    vehicle_plate = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type}"

# Customer Details model
class CustomerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"

# Trips model
class Trip(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverDetails, on_delete=models.CASCADE, null=True, blank=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=TRIP_STATUS_CHOICES, default='pending')
    trip_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Trip {self.id} - {self.status}"
