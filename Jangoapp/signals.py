from django.contrib.auth import user_logged_in,user_login_failed,user_logged_out
from .models import UserLoginActivity
from django.dispatch import receiver
import logging
from django.utils import timezone
from Jango.settings import TIME_ZONE

error_log = logging.getLogger('error')



@receiver(user_logged_in)
def log_user_logged_in_success(sender,user,request,**kwargs):
    """ User Login activity period """
    try:
        user_login_sucess=UserLoginActivity(
                                                real_name=user.username,
                                                tz=TIME_ZONE,
                                                start_time=timezone.now(),
                                                status=UserLoginActivity.SUCCESS
                                            )


        user_login_sucess.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))
import datetime
@receiver(user_logged_out)
def log_user_logged_out(sender,user,request,**kwargs):
    """ User Logout Activity period """
    try:
        user_logout_sucess=UserLoginActivity(
                                            real_name=user.username,
                                            tz=TIME_ZONE,
                                            end_time=timezone.now(),
                                            status=UserLoginActivity.LOGOUT
                                        )

        user_logout_sucess.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

@receiver(user_login_failed)
def log_user_logged_in_failed(sender,credentials,request,**kwargs):
    """ User login in failed Activity period """
    try:
        user_logout_sucess=UserLoginActivity(
                                            real_name=credentials['username'],
                                            tz=TIME_ZONE,
                                            start_time=timezone.now(),
                                            end_time=timezone.now(),
                                            status=UserLoginActivity.FAILED)

        user_logout_sucess.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))
