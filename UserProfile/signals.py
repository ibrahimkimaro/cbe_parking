# signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from authentication.models import User
# from .models import UserProfile

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance, name=instance.email)
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     else:
#         instance.user.save()