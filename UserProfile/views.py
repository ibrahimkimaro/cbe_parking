from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User 
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerilizer
from .models import UserProfile
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
import base64
import uuid
import os
from django.core.files.base import ContentFile
# Create your views here.

# This class use to check the email that stored in front_end(client_storage.get) adn email in database 
# if are equevalent it take taha data and desplay in the py flet 
  
class verify_email(APIView):
    def post(self,request,format=None):
        "APIView to verify email and retuen user details"
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            # send the back the user details if email matches here the data you want
            return Response({
                "id":user.id,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email,
                "phone_number":user.phone_number,
                             })

        except User.DoesNotExist:
           return Response({"error": "User does not exist"},status=status.HTTP_400_BAD_REQUEST)

# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication,TokenAuthentication])
class UserProfileView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    serializer_class = UserProfileSerilizer
    # permission_classes=[IsAuthenticated]
    
    def patch(self, request, user_id):
        user = User.objects.get(id=user_id)
        try:
          user_profile,create = UserProfile.objects.get_or_create(user=user)
        
        except UserProfile.DoesNotExist:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message':'User does not exists'})
        
        new_profile_pic = request.data.get('profile_pic',user_profile)
        path = os.path.basename(new_profile_pic.read())
        print(path)
        encode = base64.b64encode(path).decode('utf-8')
        print(encode)
        #file_type = data.get("profile_pic", {}).get("type").split("/")[-1].lower()
        # neww = (,user_profile)
        dec = base64.b64decode(encode).decode('utf-8')
        print(dec)
        #image_name = dec
        image_name = dec
        image_content = ContentFile(dec,name=dec)
        #user_profile.profile_pic.save()
        user_profile.profile_pic = image_content
        user_profile.save()
        return Response({'status': status.HTTP_200_OK, 'message': 'Successfully Updated'})
    
    # def patch(self, request, user_id):
    #     try:
    #         user = User.objects.get(id=user_id)
    #         user_profile, created = UserProfile.objects.get_or_create(user=user)
    #     except UserProfile.DoesNotExist:
    #         return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'User does not exist'})
            
    # # Get the uploaded image file
    #     uploaded_file = request.data.get('profile_pic')
    #     if uploaded_file:
    #     # Read the content of the uploaded file
    #         file_content = uploaded_file.read()
    #     # Encode the file content to Base64
    #         encoded_content = base64.b64encode(file_content).decode('utf-8')
    #     # Decode the Base64 string to get the original file content
    #         decoded_content = base64.b64decode(encoded_content)
    #     # Create a ContentFile with the decoded content and the original file name
    #         content_file = ContentFile(decoded_content, name=uploaded_file.name)
    #     # Save the ContentFile to the profile_pic field of the user profile
    #         user_profile.profile_pic.save(uploaded_file.name, content_file, save=True)
    #         user_profile.save()
    #         return Response({'status': status.HTTP_200_OK, 'message': 'Profile picture updated successfully'})
    #     else:
    #         return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'No profile picture provided'})


        # serializer = UserProfileSerilizer(user_profile, many=False)
        # serializer.save()
        
       

       
        # try:
        #     data = request.data
        #     user = User.objects.get(id=user_id)
        #     institution,create = UserProfile.objects.get_or_create(user=user)
            
            
        #     uploaded_file = request.data.get('profile_pic',institution)
        #     image_name = data.get("profile_pic", {}).get("name", "default.jpg")
        #     file_type = data.get("profile_pic", {}).get("type").split("/")[-1].lower()

        #     if file_type not in ["jpeg", "png", "gif", "pdf"]:
        #         print(f"File type is: %s" % file_type)
        #         return Response({"detail": "Unsupported file type"})
            
        #     decoded_data = base64.b64decode(uploaded_file)
        #     print(f"decodec:{decoded_data}")
        #     image_content = ContentFile(decoded_data, name=image_name)
        #     institution.profile_pic.save(image_name, image_content, save=True)
        #     institution.save()

        #     return Response(
        #         {
        #             "status": 200,
        #             "message": "Image Updated Successfully",
        #             #"data": serializer.data
        #         }
        #     )

        # except Exception as e:
        #     return Response(
        #         {"status": 500, "message": f"Internal Server Error: {str(e)}"}
        #     )


class plateNumberView(APIView):
    def patch(self, request, user_id):
        user = User.objects.get(id=user_id)
        try:
          user_profile,create = UserProfile.objects.get_or_create(user=user)
        
        except UserProfile.DoesNotExist:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message':'User does not exists'})
        
        new_plate_number = request.data.get('plate_number',user_profile)
        user_profile.plate_number = new_plate_number
        user_profile.save()
          
        return Response({'status': status.HTTP_200_OK, 'message': 'Successfully Updated',
                         'plate_number': user_profile.plate_number
                         })

class UserProfileLISTView(APIView):
    def get(self, request,user_id):
        user =User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerilizer(user_profile)
        return Response(serializer.data)
        
       
# class UserProfileLISTView(APIView):
    
#     def get(self,request,*args, **kwargs):
        
#         image = UserProfile.objects.all()
#         serializer = UserProfileSerilizer(image,context={'request':request},many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
            
        