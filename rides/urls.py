from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, DriverDetailsViewSet, CustomerDetailsViewSet, TripViewSet, register, login_view, logout_view

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'drivers', DriverDetailsViewSet)
router.register(r'customers', CustomerDetailsViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
