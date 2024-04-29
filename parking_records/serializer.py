from rest_framework import serializers
from authentication.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','status_type')  # Include the status field in the serializer


class parking_response(serializers.ModelSerializer ):
    #id = serializers.IntegerField()
    class Meta:
        model = User
        fields = '__all__'
        
class ParkingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingRequest
        fileds = '__all__'
        exclude = ['id']