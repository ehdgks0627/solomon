from django.test import TestCase
from .models import Review
from product.models import Category, Product
from user.models import Account
from solomon.utils import *


class QuestionMethodTests(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            id=random_string(), password='test', name='Kim', email='a@a.com', nickname='test', phone='010-0101-0101')
        self.user.save()

    def test_create_review(self):
        title = random_string()
        content = random_string()
        star = random_int(min=0, max=5)
        review = Review(title=title, content=content, star=star)
        review.save()

        self.assertNotEqual(review, None)
        self.assertEqual(review.title, title)
        self.assertEqual(review.content, content)
        self.assertEqual(review.star, star)


class QuestionViewTests(TestCase):
    pass
