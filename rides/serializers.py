from rest_framework import serializers
from .models import Profile, DriverDetails, CustomerDetails, Trip

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DriverDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails
        fields = '__all__'

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
