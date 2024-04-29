from django.urls import path
from . import views

urlpatterns = [
    path('guardinList/', views.SecuritytUserView.as_view(), name='guardins-users'),
    path('login/',views.LoginView.as_view(), name='login'),
    path('user/<int:user_id>/',views.UserSpecific.as_view(), name='login'),
    path('user-parking-request/', views.UserParking_in_RequestAPIView.as_view(), name='user parking Request'),
    path('sign-out/', views.UserParking_out_RequestAPIView.as_view(), name='parking_Out'),
    path('mlinziview/', views.MlinziViewAllTheRequestAPIView.as_view(), name='mlinzi View'),
    path('mlinziApproveUser/<int:user_id>/', views.MlinziApproveRequestAPIView.as_view(), name=' parking Request Approver'),
    path('mlinziReject/<int:user_id>/', views.RejectUserView.as_view(), name='Mlinzi Rejecte User'),
    path('specific-user/<int:user_id>/', views.SpecifUser.as_view(), name='SPECIFIC USER DETAILS'),
    path('user-response/<int:user_id>/', views.UserResponse.as_view(), name='parking_out'),
    path('details/<int:user_id>/', views.user_see_parking_records.as_view(), name='parking details list'),
    
]

