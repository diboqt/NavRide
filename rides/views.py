from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile, DriverDetails, CustomerDetails, Trip
from .serializers import ProfileSerializer, DriverDetailsSerializer, CustomerDetailsSerializer, TripSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # If you want users to be authenticated to call login, remove this line if not
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return JsonResponse({'message': 'Email and password are required'}, status=400)

    # Use Django's authenticate method to verify user
    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)  # Creates session for the user
        return JsonResponse({'message': 'Login successful', 'user_id': user.id})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=400)

def logout_view(request):
    logout(request)  # End the session
    return JsonResponse({'message': 'Logout successful'})


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')
    
    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists"}, status=400)
    
    if User.objects.filter(email=email).exists():
        return Response({"message": "Email already exists"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    # Add custom fields for 'role' if necessary
    # user.profile.role = role  # Assuming you have a Profile model for the role
    # user.save()

    return Response({"message": "Registration successful"}, status=200)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DriverDetailsViewSet(viewsets.ModelViewSet):
    queryset = DriverDetails.objects.all()
    serializer_class = DriverDetailsSerializer


class CustomerDetailsViewSet(viewsets.ModelViewSet):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['post'])
    def assign_driver(self, request, pk=None):
        trip = self.get_object()
        try:
            driver = DriverDetails.objects.get(user=request.user)
            if trip.status == 'pending' and driver.availability:
                trip.driver = driver
                trip.status = 'in_progress'
                trip.save()
                return Response({'status': 'Driver assigned successfully'})
            return Response({'error': 'Trip already in progress or driver not available'}, status=status.HTTP_400_BAD_REQUEST)
        except DriverDetails.DoesNotExist:
            return Response({'error': 'Only drivers can accept trips'}, status=status.HTTP_403_FORBIDDEN)
