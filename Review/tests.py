from django.test import TestCase
from .models import Review
from Product.models import Category, Product
from User.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password='test', email='a@a.com', nickname='test', phone='010-0101-0101')
        self.product = Product(
            owner=self.user, title='test_title', content='test_content', one_line_introduce='test_one_line_introduce',
            category=random_choice(Category.get_all_category_code(Category)),
            as_rule='test_as_rule', refund_rule='test_refund_rule')
        self.user.save()
        self.product.save()


    def test_create_review(self):
        owner = self.user
        product = self.product
        title = random_string()
        content = random_string()
        star = random_int(min=0, max=5)
        review = Review(owner=owner, product=product, title=title, content=content, star=star)
        review.save()

        self.assertNotEqual(review, None)
        self.assertEqual(review.owner, self.user)
        self.assertEqual(review.title, title)
        self.assertEqual(review.content, content)
        self.assertEqual(review.star, star)


class QuestionViewTests(TestCase):
    pass
