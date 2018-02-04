from django.test import TestCase
from Order.models import Order
from .models import Contact
from User.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password="test", email="a@a.com", nickname="test", phone="010-0101-0101")
        self.user.save()

    def test_create_contact(self):
        owner = self.user
        title = random_string()
        content = random_string()
        order = None

        contact = Contact(owner=owner, title=title, content=content, order=order)
        contact.save()

        self.assertNotEqual(contact, None)
        self.assertEqual(contact.owner, self.user)
        self.assertEqual(contact.title, title)
        self.assertEqual(contact.content, content)
        self.assertEqual(contact.order, order)


class QuestionViewTests(TestCase):
    pass
