from django.db import models
from authentication.models import User
from datetime import timedelta,timezone
        
class ParkingRequest(models.Model):
    
    PARKINGSTATUS = (
    (1, 'Pending'),
    (2, 'accepted'),
    (3, 'rejected'),
)
    # user id is for both mlinzi and user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ## utabidi ubadilishe TimeFile kunwa DateTimeField kupata tarehe na muda..ukija kutengeneza db mpya
    reportTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    departureTime = models.DateTimeField(null=True, blank=True)
    status_request = models.IntegerField(default=1, choices=PARKINGSTATUS, null=True, blank=True)

    
    def save(self, *args, **kwargs):
        if self.user.status_type != 'security':
            super().save(*args, **kwargs)
        else:
            raise ValueError("UserProfile cannot be created for users with 'security' status.")
    