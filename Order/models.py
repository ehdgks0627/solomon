from django.db import models
from User.models import Account
from Product.models import Product
from Project.models import Project
from Contract.models import Contract
from Review.models import Review


class Order(models.Model):
    STATE_CHOICE = (
        (1, '결제 대기'),
        (2, '진행 대기'),
        (3, '진행 중'),
        (4, '검수 중'),
        (5, '검수 완료'),
        (6, '완료'),
        (7, '취소 요청'),
        (8, '취소'),
    )

    # TODO 추가하기
    PAYMENT_CHOICE = (

    )

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    seller = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    state = models.IntegerField(
        blank=False,
        null=False,
        default=1  # 결제 대기
    )

    # 판매자에게 보여주지 않기
    payment_method = models.IntegerField(
        blank=False,
        null=False
    )

    price = models.IntegerField(
        blank=False,
        null=False
    )

    period = models.IntegerField(
        blank=False,
        null=False
    )

    # 판매자가 등록 할 수 있게끔, 추후에 판매자 분류 및 프로젝트 조회때 사용됨
    tags = models.TextField(
        blank=False,
        null=False,
        default='[]'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['owner', 'seller', 'product', 'project', 'contract', 'review', 'state', 'payment_method',
                       'price', 'period', 'tags']
