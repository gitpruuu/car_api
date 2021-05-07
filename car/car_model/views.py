from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from car.car_model.serializers import CarSerializer, CarModelSerializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarModelViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]