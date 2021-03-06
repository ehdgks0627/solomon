from django.test import TestCase
from .models import Order
from project.models import Project
from product.models import Product, Category
from user.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password='test', name='Kim', email='a@a.com', nickname='test', phone='010-0101-0101')
        self.user.save()

        self.user2 = Account.objects.create_user(
            id=random_string(), password='test2', name='Hong', email='a@b.com', nickname='test2', phone='010-0101-0102')
        self.user2.save()

        self.product = Product(
            owner=self.user, title='test_title', content='test_content', one_line_introduce='test_one_line_introduce',
            category=random_choice(Category.get_all_category_code(Category)),
            as_rule='test_as_rule', refund_rule='test_refund_rule')
        self.product.save()

        self.project = Project(
            title='test_title', description='test_description',
            price=5000, period=3, owner=self.user,
            category=random_choice(Category.get_all_category_code(Category)))
        self.project.save()

    def test_create_order(self):
        owner = self.user
        product = self.product
        project = self.project
        title = random_string()
        state = Order.STATE_CHOICE[random_choice(base=list(Order.STATE_CHOICE.keys()))]
        payment_method = 1  # TODO 결제 방법
        price = random_int(min=50000, max=5000000)
        period = random_int(min=0, max=100)
        tags = []
        for _ in range(5):
            tags.append(random_string())

        order = Order.objects.create_order(owner=owner, product=product, project=project, title=title, state=state,
                                           payment_method=payment_method,
                                           price=price, period=period, tags=tags)
        self.order = order

        self.assertNotEqual(order, None)
        self.assertEqual(order.owner, self.user)
        self.assertEqual(order.product, product)
        self.assertEqual(order.project, project)
        self.assertEqual(order.title, title)
        self.assertEqual(order.state, state)
        self.assertEqual(order.payment_method, payment_method)
        self.assertEqual(order.price, price)
        self.assertEqual(order.period, period)
        self.assertEqual(order.tags, tags)

    def test_order_state(self):
        owner = self.user
        product = self.product
        project = self.project
        state = Order.STATE_CHOICE['결제 대기']
        payment_method = 1  # TODO 결제 방법
        price = random_int(min=50000, max=5000000)
        period = random_int(min=0, max=100)
        tags = []
        for _ in range(5):
            tags.append(random_string())

        self.order = Order.objects.create_order(owner=owner, product=product, project=project, state=state,
                                                payment_method=payment_method, price=price, period=period, tags=tags)
        self.assertEqual(self.order.change_state('진행 대기'), True)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['진행 대기'])
        self.assertEqual(self.order.change_state('결제 대기'), False)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['진행 대기'])
        self.assertEqual(self.order.change_state('진행 중'), True)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['진행 중'])
        self.assertEqual(self.order.change_state('취소 요청'), True)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['취소 요청'])
        self.assertEqual(self.order.change_state('취소'), True)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['취소'])
        self.assertEqual(self.order.change_state('완료'), False)
        self.assertEqual(self.order.state, Order.STATE_CHOICE['취소'])


class QuestionViewTests(TestCase):
    pass
