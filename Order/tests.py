from django.test import TestCase
from Project.models import Project
from Product.models import Product, Category
from .models import Order
from User.models import Account
from solomon.utils import *
import json


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password="test", email="a@a.com", nickname="test", phone="010-0101-0101")
        self.user2 = Account.objects.create_user(
            id=random_string(), password="test2", email="a@b.com", nickname="test2", phone="010-0101-0102")
        self.product = Product(
            owner=self.user, title="test_title", content="test_content", one_line_introduce="test_one_line_introduce",
            category=random_choice(Category.get_all_category_code(Category)),
            as_rule="test_as_rule", refund_rule="test_refund_rule", period_sensitivity=random_int(min=0, max=10))
        self.project = Project(
            title="test_title", description="test_description", price=5000, period=3, owner=self.user)
        self.user.save()
        self.user2.save()
        self.product.save()
        self.project.save()

    def test_create_order(self):
        owner = self.user
        product = self.product
        project = self.project
        state = Order.STATE_CHOICE[random_choice(base=list(Order.STATE_CHOICE.keys()))]
        payment_method = 1  # TODO 결제 방법
        price = random_int(min=50000, max=5000000)
        period = random_int(min=0, max=100)
        tags = []
        for _ in range(5):
            tags.append(random_string())

        order = Order(owner=owner, product=product, project=project, state=state, payment_method=payment_method,
                      price=price, period=period, tags=json.dumps(tags))
        order.save()
        self.order = order

        self.assertNotEqual(order, None)
        self.assertEqual(order.owner, self.user)
        self.assertEqual(order.product, product)
        self.assertEqual(order.project, project)
        self.assertEqual(order.state, state)
        self.assertEqual(order.payment_method, payment_method)
        self.assertEqual(order.price, price)
        self.assertEqual(order.period, period)
        self.assertEqual(json.loads(order.tags), tags)

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

        self.order = Order(owner=owner, product=product, project=project, state=state, payment_method=payment_method,
                           price=price, period=period, tags=json.dumps(tags))
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


STATE_CHOICE = {
    '결제 대기': 10,
    '진행 대기': 20,
    '진행 중': 21,
    '검수 중': 30,
    '검수 완료': 31,
    '완료': 40,
    '취소 요청': 100,
    '취소': 101,
}


class QuestionViewTests(TestCase):
    pass
