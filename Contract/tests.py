from django.test import TestCase
from Project.models import Project
from Product.models import Product, Category
from .models import Order
from User.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password='test', email='a@a.com', name='Kim', nickname='test', phone='010-0101-0101')
        self.user.save()

        self.user2 = Account.objects.create_user(
            id=random_string(), password='test2', email='a@b.com', name='Hong', nickname='test2', phone='010-0101-0102')
        self.user2.save()

        self.product = Product(
            owner=self.user, title='test_title', content='test_content', one_line_introduce='test_one_line_introduce',
            category=random_choice(Category.get_all_category_code(Category)),
            as_rule='test_as_rule', refund_rule='test_refund_rule')
        self.product.save()

        self.project = Project(
            title='test_title', description='test_description', price=5000, period=3, owner=self.user)
        self.project.save()

        self.order = Order(
            owner=self.user,
            product=self.product,
            project=self.project,
            title=random_string(),
            state=Order.STATE_CHOICE[random_choice(base=list(Order.STATE_CHOICE.keys()))],
            payment_method=1,
            price=50000,
            period=3,
            tags=['1', '2', '3']
        )
        self.order.save()

    def test_create_contract(self):
        pass


class QuestionViewTests(TestCase):
    pass
