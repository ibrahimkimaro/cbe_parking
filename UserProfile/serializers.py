from rest_framework import serializers
from .models import UserProfile
# from django import forms

class UserProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exlude = ['user']
    
    # def create(self,validate_data):
    #     image =  UserProfile.objects.create(
    #         profile_pic = validate_data["profile_pic"],
    #         )
    #     return image
    
    # def get_image_rl(self,obj):
    #     request = self.context.get('request')
    #     imge_url = obj.fingerprint.url
    #     return request.build_absolute_uri(imge_url)
    
    # def create(self,validated_data):
    #     profile_pic = UserProfile.objects.create(
    #         profile_pic = validated_data['profile_pic']
    #         )
    #     return profile_pic