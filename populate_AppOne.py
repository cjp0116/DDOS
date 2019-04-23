from faker import Factory
from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProOne.settings')

import django
django.setup()

## Create the fake population script
import random
from AppOne.models import Users, Topic, Webpage, Access

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topics():
    t= Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get a topic for that entry
        top = add_topics()

        #  Create a fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        fake_name2 = fakegen.name().split()
        fake_first = fake_name2[0]
        fake_last = fake_name2[1]
        fake_email = fakegen.email()

        users = Users.objects.get_or_create(first_name = fake_first,
                                           last_name = fake_last,
                                           email = fake_email)

        #  Create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #  Create a fake access record for tha webpage
        acc_rec = Access.objects.get_or_create(name = webpg, date= fake_date)[0]



if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population complete!')

