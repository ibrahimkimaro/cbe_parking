from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('register/',views.UserRegistrationAPIView.as_view(),name="User Registration"),
    path('registeredData/<int:user_id>/',views.getUserRegisrationsData.as_view(),name="YOUR user registered"),
    path('logout/',views.user_logout,name="User login"),
    path('userauth/',views.veryfiy_user_authentication,name="Verify the token"),
    path('login/',views.UserloginAPI.as_view(),name="LOGIN PAGE"),
    path('user_id/',views.get_user_id,name="User Identity")
    
    
]
