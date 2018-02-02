from django.test import TestCase
from .models import Project
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def test_create_project(self):
        title = random_string()
        description = random_string()
        price = random_int()
        period = random_int()
        project = Project(
            title=title, description=description, price=price, period=period)
        project.save()

        self.assertNotEqual(project, None)
        self.assertEqual(project.title, title)
        self.assertEqual(project.description, description)
        self.assertEqual(project.price, price)
        self.assertEqual(project.period, period)

        project.delete()


class QuestionViewTests(TestCase):
    pass
