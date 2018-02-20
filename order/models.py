from django.db import models
from contract.models import Contract
from review.models import Review
from django.utils import timezone
import ujson


class OrderManager(models.Manager):
    def create_order(self, project, title=None, price=None, period=None, tags=None, **kwargs):
        if not title:
            title = project.title
        if not price:
            price = project.price
        if not period:
            period = project.period
        contract = Contract.objects.create_contract()
        order = self.model(project=project, contract=contract, title=title, price=price, period=period, **kwargs)
        if tags:
            order.tags = tags
        order.save()
        return order


class Order(models.Model):
    objects = OrderManager()

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
        'user.Account',
        related_name='%(app_label)s_%(class)s_owner',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    product = models.ForeignKey(
        'product.Product',
        related_name='%(app_label)s_%(class)s_produc',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    project = models.ForeignKey(
        'project.Project',
        related_name='%(app_label)s_%(class)s_project',
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
        'contract.Contract',
        related_name='%(app_label)s_%(class)s_contract',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    review = models.OneToOneField(
        'review.Review',
        related_name='%(app_label)s_%(class)s_review',
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
        return ujson.loads(self._tags)

    @tags.setter
    def tags(self, value):
        self._tags = ujson.dumps(value)

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
            self.begin_at = timezone.now()
        self.save()
        return True

    def write_review(self, title, content, star, tags=None):
        if self.review:
            return False
        self.review = Review.objects.create_review(title=title, content=content, star=star, tags=tags)
        self.save()
