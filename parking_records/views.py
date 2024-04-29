from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from authentication.models import User
from UserProfile.models import UserProfile
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import  ParkingRequest
from django.utils import timezone
from rest_framework import status
from django.http import JsonResponse
from .serializer import ParkingRequestSerializer
import random 
from datetime import timedelta
import asyncio,datetime


class SecuritytUserView(APIView):
    def get(self, request):
        guardian = User.objects.filter(status_type='security')  # Filter users based on status
        serializer = UserSerializer(guardian, many=True)
        return Response(serializer.data)

class UserSpecific(APIView):
    def get(self, request,user_id):
        user =User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password,)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

# here i start to handle parking request and response from user-guardian and verse-versa
        

class UserParking_in_RequestAPIView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get('user_id',None)
        try:
            user = User.objects.get(id=user_id)
            
        except User.DoesNotExist:
            return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
        
        user_request = ParkingRequest.objects.create(
            user=user,
        )
        #user_request.departureTime
        user_request.status_request = 1
        user_request.save()
        
        if (user_request.status_request == 2) == (timedelta(seconds=5)):
            user_request.delete()
        
        return Response({'message':'Successfully created'},status=status.HTTP_201_CREATED)
    
# This class use to handle the sign-out of a user
# This is arequest from user to mlinzi
class UserParking_out_RequestAPIView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get('user_id',None)
        try:
            user = User.objects.get(id=user_id)
            
        except User.DoesNotExist:
            return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
        
        user_request = ParkingRequest.objects.filter(
            user = user
        ).last()
        
        if user_request.status_request == 2:
            user_request.departureTime = timezone.now()
            user_request.save()
            return Response({'message':'Successfly sighn Out'},status=status.HTTP_200_OK)
        else:
            return Response({'message':"You have not in our parking list"})
        
# Mlinzi akivuta request iliyoingia ya mwisho kutoka kwa user      
class MlinziViewAllTheRequestAPIView(APIView):
     def get(self, request):
        # try:
        #     user = User.objects.get(id=request.data.user.id)
        # except User.DoesNotExist:
        #     return Response({"message": "User not found"}, status=400)
        
        parking_requests = ParkingRequest.objects.filter(status_request = 1).last()
        serializer = ParkingRequestSerializer(parking_requests)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Mlinzi akivuta taarifa za user mmoja aliyetuma request kwajili ya parking  
# Here we can pass the id of a user aliyetuma request na id ake tunaipata kupitia class ya MlinziViewAllRequestView
class SpecifUser(APIView):
    def get(self,request,user_id):
        user = User.objects.get(id=user_id)
        profile = UserProfile.objects.get(user=user_id)
        return Response(
            {
                "first_name":user.first_name,
                "last_name":user.last_name,
                "phone_number":user.phone_number,
                "status":user.status,
                "plate_number":profile.plate_number
            }
        )

# Mlinzi akikubali user aingie
class MlinziApproveRequestAPIView(APIView):
    def get(self, request,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Request not found"}, status=400)
        
        
        parkingRequest= ParkingRequest.objects.filter(user=user).last()
        parkingRequest.status_request = 2
        parkingRequest.save()
        return Response({"message": "Request Accepted...Please you can enter"}, status=status.HTTP_200_OK)

# Mlinzi akikataa user aiingie na kufuta data zake
class RejectUserView(APIView):
     def get(self, request,user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Request not found"}, status=400)
        
        
        parkingRequest= ParkingRequest.objects.filter(user=user).last()
        parkingRequest.status_request = 3
        parkingRequest.delete()
        return Response({"message": "CLear Usr Rejected"}, status=status.HTTP_200_OK)
    

# User akipata majibu baada a mlinzi kufanya responde
class UserResponse(APIView):
    def get(self,request,user_id):
        try:
            user = ParkingRequest.objects.get(user=user_id)
            
        except User.DoesNotExist:
            return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
        
        if user.status_request == 1:
            return Response({"message":"Your requst has pending"})
        elif user.status_request == 2:
            return Response({"message":"You have accepted..Please You can Enter"},status=status.HTTP_202_ACCEPTED)
        elif user.status_request == 3:
            return Response({"message":"You have rejected"},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error":"Invalid User"},status=status.HTTP_404_NOT_FOUND)

class user_see_parking_records(APIView):
    def get(self,request,user_id):
        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return Response({"message": "Request not found"}, status=400)
        
        user = User.objects.get(id=user_id)
        parking_requet  = ParkingRequest.objects.filter(user=user,status_request=2)
        ser = ParkingRequestSerializer(parking_requet,many=True)
        #return Response(ser.data,{"fist_name": user.})
        return Response(
            {
                "first_name": user.first_name,
                 "last_name": user.last_name,
                "user_data": ser.data
            },
            )

        