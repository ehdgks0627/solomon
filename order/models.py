from django.db import models
from contract.models import Contract
from user.models import Account
from product.models import Product
from project.models import Project
from review.models import Review
import datetime
import json


class Order(models.Model):
    def __init__(self, tags=None, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        if tags:
            self.tags = tags
            # self.save()

    STATE_CHOICE = {
        '계약서 작업': 10,
        '결제 대기': 20,
        '진행 대기': 30,
        '진행 중': 31,
        '검수 중': 40,
        '검수 완료': 41,
        '완료': 50,
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
        related_name='%(app_label)s_%(class)s_owner'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=256,
        blank=False,
        null=False
    )

    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        blank=False,
        null=False
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
        default=STATE_CHOICE['계약서 작업']  # 결제 대기
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
    _tags = models.TextField(
        blank=False,
        null=False,
        default='[]'
    )

    @property
    def tags(self):
        return json.loads(self._tags)

    @tags.setter
    def tags(self, value):
        self._tags = json.dumps(value)

    begin_at = models.DateTimeField(
        blank=True,
        null=True,
        default=None
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def change_state(self, state):
        if state not in self.STATE_CHOICE:
            return False
        if self.state > self.STATE_CHOICE[state]:
            return False
        self.state = self.STATE_CHOICE[state]

        if self.state == self.STATE_CHOICE['진행 중']:
            self.begin_at = datetime.datetime.now()
        self.save()
        return True
