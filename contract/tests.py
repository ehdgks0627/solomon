from django.test import TestCase
from .models import Contract
from order.models import Order
from project.models import Project
from product.models import Product, Category
from user.models import Account
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
            title='test_title', description='test_description',
            price=5000, period=3, owner=self.user,
            category=random_choice(Category.get_all_category_code(Category)))
        self.project.save()

        self.order = Order.objects.create_order(
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
        buyer_agreement = random_bool()
        seller_agreement = random_bool()
        buyer_signature = random_string()

        contract = Contract.objects.create_contract(buyer_agreement=buyer_agreement,
                                                    seller_agreement=seller_agreement,
                                                    buyer_signature=buyer_signature)

        self.assertEqual(contract.buyer_agreement, buyer_agreement)
        self.assertEqual(contract.seller_agreement, seller_agreement)

        for _ in range(20):
            contract.buyer_agreement = random_bool()
            contract.seller_agreement = random_bool()
            contract.save()
            contract.reset_agreement()
            self.assertEqual(contract.buyer_agreement, False)
            self.assertEqual(contract.seller_agreement, False)

        self.assertEqual(contract.clause['max_id'], 1)
        self.assertEqual(len(contract.clause['clauses']), 0)

        self.assertEqual(contract.add_clause(1, "A"), False)
        self.assertEqual(contract.clause['max_id'], 1)
        self.assertEqual(len(contract.clause['clauses']), 0)

        self.assertEqual(contract.add_step_clause('1', 12.34), True)
        self.assertEqual(contract.clause['max_id'], 1)
        self.assertEqual(len(contract.clause['clauses']), 1)

        self.assertEqual(contract.clause['clauses']['1']['fee'], 12.34)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), 0)

        self.assertEqual(contract.add_step_clause('1', 12.34), False)
        self.assertEqual(contract.clause['max_id'], 1)
        self.assertEqual(len(contract.clause['clauses']), 1)

        self.assertEqual(contract.clause['clauses']['1']['fee'], 12.34)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), 0)

        get_content = lambda item: item['content']

        before_max_id = contract.clause['max_id']
        content = random_string()
        self.assertEqual(contract.add_clause('1', content), True)
        self.assertEqual(content in map(get_content, contract.clause['clauses']['1']['data']), True)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), 1)
        self.assertEqual(before_max_id + 1, contract.clause['max_id'])

        self.assertEqual(contract.add_clause('2', content), False)
        self.assertEqual(content in map(get_content, contract.clause['clauses']['1']['data']), True)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), 1)
        self.assertEqual(before_max_id + 1, contract.clause['max_id'])

        for step in range(20):
            before_max_id = contract.clause['max_id']
            content = random_string()
            self.assertEqual(contract.add_clause('1', content), True)
            self.assertEqual(content in map(get_content, contract.clause['clauses']['1']['data']), True)
            self.assertEqual(len(contract.clause['clauses']['1']['data']), 2 + step)
            self.assertEqual(before_max_id + 1, contract.clause['max_id'])

        self.assertEqual(contract.del_clause(0), False)
        self.assertEqual(contract.del_clause(1), True)
        self.assertEqual(contract.del_clause(1), False)
        self.assertEqual(contract.del_clause(-1), False)

        before_length = len(contract.clause['clauses']['1']['data'])
        self.assertEqual(contract.del_clause(1), False)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), before_length)
        self.assertEqual(contract.del_clause(2), True)
        self.assertEqual(len(contract.clause['clauses']['1']['data']), before_length - 1)

        self.assertEqual(contract.add_step_clause('2', 34), True)
        self.assertEqual(contract.add_step_clause('3', 35), True)
        self.assertEqual(contract.add_step_clause('4', 36), True)

        self.assertEqual(contract.add_clause(5, content), False)

        self.assertEqual(len(contract.clause['clauses']), 4)


class QuestionViewTests(TestCase):
    pass
