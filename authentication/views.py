from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserRegistration,Userlogin
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

#from knox.models import k Auth

#Create your views here.


class UserRegistrationAPIView(APIView):
    def post(self,request):  
        serializer = UserRegistration(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=request.data['email'])
            token = Token.objects.create(user=user)
            return Response({"tokne":token.key,"user":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
@api_view(['GET'])
def get_user_id(request):
    user,create = User.objects.get_or_create(id=request.user.id)
    return Response({
        "id": user.id,
    })
      
class getUserRegisrationsData(APIView):
    def get(self,request,user_id):
        queryset = User.objects.get(id=user_id)
        serilizer = UserRegistration(queryset)
        
        return Response(serilizer.data)
    
class UserloginAPI(APIView):
    def post(self,request):  
        serializer = Userlogin(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token,create = Token.objects.get_or_create(user=user)
            # Perform any additinal action  if neede such as generating token
            return Response({"Token":token.key,"user":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response("user have been login out")

#Ni view tunatotumia kutuma maombi ya kubadilisha password kweny server
# class PasswordResetView(APIView):
#     def post(self,request):
#         serializer = PasswordResetRequest(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.validated_data.get('email')
        
#         user = User.objects.get(email=email)
#         if user:
#             return Response({"message":"the email is satisfied"},status=status.HTTP_200_OK)
#         else:
#             return Response({"Error":"invalid email"},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def veryfiy_user_authentication(request):
    return Response("Authenticated for {}".format(request.user.email))

