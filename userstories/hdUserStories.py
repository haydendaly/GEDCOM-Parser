import unittest
from datetime import datetime, timedelta

def us_35(people_list):
    recent = []
    for person in people_list:
        if(person.birthday >> datetime.datetime.now() + datetime.timedelta(-30)):
            recent.append(person.id)
    print(recent)
    return recent

def test():
    print('test')
