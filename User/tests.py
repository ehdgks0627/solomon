from django.test import TestCase
from .models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def test_create_user(self):
        id = random_string()
        email = random_string() + "@" + random_string(only_lower=True) + ".com"
        nickname = random_string()
        phone = random_string(only_digit=True)
        password = Account.objects.make_random_password()
        is_active = random_bool()
        user = Account.objects.create_account(
            id=id, email=email, nickname=nickname, phone=phone, password=password)

        self.assertNotEqual(user, None)
        user.is_active = is_active
        self.assertEqual(user.id, id)
        self.assertEqual(user.email, email)
        self.assertEqual(user.nickname, nickname)
        self.assertEqual(user.phone, phone)
        self.assertEqual(user.is_active, is_active)
        self.assertEqual(user.is_staff, False)

    def test_create_super_user(self):
        id = random_string()
        email = random_string() + "@" + random_string(only_lower=True) + ".com"
        nickname = random_string()
        phone = random_string(only_digit=True)
        password = Account.objects.make_random_password()
        is_active = random_bool()
        super_user = Account.objects.create_superuser(
            id=id, email=email, nickname=nickname, phone=phone, password=password)

        self.assertNotEqual(super_user, None)
        super_user.is_active = is_active
        self.assertEqual(super_user.id, id)
        self.assertEqual(super_user.email, email)
        self.assertEqual(super_user.nickname, nickname)
        self.assertEqual(super_user.phone, phone)
        self.assertEqual(super_user.is_active, is_active)
        self.assertEqual(super_user.is_staff, True)


class QuestionViewTests(TestCase):
    pass
