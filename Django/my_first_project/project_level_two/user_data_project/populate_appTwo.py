import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_data_project.settings')

import django
django.setup()
import random
from appTwo.models import User
from faker import Faker

fakegen =Faker()

def populate(N=5):
    for _ in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]


if __name__ == '__main__':
    print("populating the database....")
    populate(20)
    print("Population complete!")
