from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
#from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# if the error rise for this model Yount to chnage in User and write settings.AUTH_USER_MODEL
# and import settings above 
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic = models.ImageField(upload_to='profile_pic/',blank=True,null=True)
    plate_number = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name
    # Here i validate the login if user(status_typr) is security do not create the Userprofile
    def save(self, *args, **kwargs):
        if self.user.status_type != 'security':
            super().save(*args, **kwargs)
        else:
            raise ValueError("UserProfile cannot be created for users with 'security' status.")