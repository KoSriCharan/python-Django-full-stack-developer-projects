import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for _ in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        fake_date = fakegen.date()
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
if __name__ == '__main__':
    print("Populating the database...")
    populate(20)
    print("Population complete!")
