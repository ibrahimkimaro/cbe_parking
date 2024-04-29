from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from rest_framework.authentication import authenticate 


class UserRegistration(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    status = serializers.CharField()
    status_type = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','phone_number','status','status_type','password']
      
    # Vlidation of phone number if user enter number below 9    
    def validate_phone_number(self,value):
        if len(str(value)) <= 8:
            raise serializers.ValidationError(detail="please enter 9 digits")
        return value
    #validation of number if user enter same number as phone_number in database
   # def validate(self,attrs):
        
        # phone_number_exits = registration.objects.filter(phone_number= attrs['phone_number']).exists()
        
        # if phone_number_exits:
        #     raise serializers.ValidationError(detail="The phone_number already  existed")
    
           # return attrs
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            status=validated_data['status'],
            status_type=validated_data['status_type'],
            password=validated_data['password'],
        )
        
        return user
    
    
class Userlogin(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError(detail="User account is disabled")
            else:
                raise serializers.ValidationError(detail="just include email and password")
            return data

# class PasswordResetRequest(serializers.Serializer):
#     email = serializers.EmailField()
    
# class PasswordResetConfrim(PasswordResetConfirmSerializer):
#     token = serializers.CharField()
#     new_password =serializers.CharField()
    
   # password = serializers.CharField(min_length=4)
   
# class UserProfileserializer(serializers.Serializer):
#     class Meta:
#         model = UserProfile
#         fields = 'image'
        
#     def create(self,validated_data):
      
#         return UserProfile.objects.create(
#             **validated_data)