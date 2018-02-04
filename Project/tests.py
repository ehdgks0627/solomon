from django.test import TestCase
from .models import Project
from User.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password="test", email="a@a.com", nickname="test", phone="010-0101-0101")
        self.user.save()

    def test_create_project(self):
        title = random_string()
        description = random_string()
        price = random_int()
        period = random_int()
        project = Project(
            title=title, description=description, price=price, period=period, owner=self.user)
        project.save()

        self.assertNotEqual(project, None)
        self.assertEqual(project.title, title)
        self.assertEqual(project.description, description)
        self.assertEqual(project.price, price)
        self.assertEqual(project.period, period)
        self.assertEqual(project.owner, self.user)


class QuestionViewTests(TestCase):
    pass
