from django.urls import path
from . import views

urlpatterns = [
        path('verify_email/',views.verify_email.as_view(),name="Verify email"),
        path('image/<int:user_id>/',views.UserProfileView.as_view(),name="Upload Image"),
        path('userProfile_details/<int:user_id>/',views.UserProfileLISTView.as_view(),name="User profile details"),
        path('plate_number/<int:user_id>/',views.plateNumberView.as_view(),name="Change the plate number")
        
        
]