from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.


class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

from django.utils import timezone
class UserLoginActivity(models.Model):
    """ User login logout activities """
    # Login Status
    SUCCESS = 'S'
    LOGOUT  = 'L'
    FAILED  = 'F'


    LOGIN_STATUS = ((SUCCESS,'Success'),
                    (LOGOUT, 'LOGOUT'),
                    (FAILED, 'Failed'))
    start_time = models.DateTimeField(null=True,blank=True)
    end_time   = models.DateTimeField(null=True,blank=True)
    real_name  = models.CharField(max_length=50,blank=True,null=True)
    tz         = models.CharField(max_length=50,null=True)
    status     = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)


    class Meta:
        verbose_name        = 'user_login_activity'
        verbose_name_plural = 'user_login_activities'
    
    def __str__(self):
        return self.real_name
