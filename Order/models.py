from django.db import models
from User.models import Account
from Product.models import Product
from Project.models import Project
from Contract.models import Contract
from Review.models import Review


class Order(models.Model):
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

    # TODO 추가하기
    PAYMENT_CHOICE = (

    )

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='owner'
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

    REQUIRED_FIELDS = ['owner', 'product', 'project', 'contract', 'review', 'state', 'payment_method',
                       'price', 'period', 'tags']

    def change_state(self, state):
        if state not in self.STATE_CHOICE:
            return False
        self.state = self.STATE_CHOICE[state]
        self.save()
        return True
