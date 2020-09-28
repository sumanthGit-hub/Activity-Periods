import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Jango.settings')

import django

django.setup()

from Jangoapp.models import UserLoginActivity
from faker import Faker

fake=Faker()

def details(N=5):
""" For Dummy date Creation """
    for entry in range(N):
        fake_name=fake.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_tz=fake.city()
        fake_start=fake.date_time_this_month()
        fake_end=fake.date_time_this_month()
        name=fake_first_name+' '+fake_last_name

        user=Member.objects.get_or_create(real_name=name,tz=fake_location)[0]

if __name__=='__main__':
    print('Details Creating')
    details(5)
    print('Complete')
