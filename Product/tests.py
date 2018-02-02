from django.test import TestCase
from .models import Product, Category
from User.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_account(
            id=random_string(), password="test", email="a@a.com", nickname="test", phone="010-0101-0101")

    def test_create_project(self):
        title = random_string()
        content = random_string()
        category = random_choice(Category.get_all_category_code(Category))
        one_line_introduce = random_string()
        as_rule = random_string()
        refund_rule = random_string()
        period_sensitivity = random_int(max=10)
        product = Product(
            owner=self.user, title=title, content=content, category=category, one_line_introduce=one_line_introduce,
            as_rule=as_rule, refund_rule=refund_rule, period_sensitivity=period_sensitivity)
        product.save()

        self.assertNotEqual(product, None)
        self.assertEqual(product.owner, self.user)
        self.assertEqual(product.title, title)
        self.assertEqual(product.content, content)
        self.assertEqual(product.category, category)
        self.assertEqual(product.one_line_introduce, one_line_introduce)
        self.assertEqual(product.as_rule, as_rule)
        self.assertEqual(product.refund_rule, refund_rule)


class QuestionViewTests(TestCase):
    pass