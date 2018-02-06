from django.db import models
from User.models import Account


# Create your models here.
class Category:
    CATEGORY_CHOICES = (
        (u'소프트웨어 개발', (
            (101, u'웹사이트'),
            (102, u'안드로이드앱'),
            (103, u'아이폰'),
            (104, u'응용프로그래밍'),
            (105, u'기술지원 / 원격'),
            (106, u'임베디드'),
            (107, u'매크로'),
            (108, u'PC견적'),
            (109, u'IOT'),
            (110, u'게임'),
            (111, u'기타'),
        )
         ),
        (u'디자인', (
            (201, u'웹디자인'),
            (202, u'로고 / CI&BI'),
            (203, u'캘리그라피'),
            (204, u'전단지 / 홍보물'),
            (205, u'명함'),
            (206, u'일러스트'),
            (207, u'캐리커쳐'),
            (208, u'만화 / 웹툰'),
            (209, u'캐릭터 / 아이콘'),
            (210, u'패키지'),
            (211, u'인테리어'),
            (222, u'3D'),
            (223, u'PPT'),
            (224, u'포토샵'),
            (225, u'사진촬영'),
            (226, u'누끼작업'),
            (227, u'기타'),
        )
         )
    )

    def get_all_category_code(self):
        categories = []
        for cat in self.CATEGORY_CHOICES:
            for item in cat[1]:
                categories.append(item[0])

        return categories


class Product(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    img = models.ImageField(
        null=True,
        blank=True,
        upload_to='image/img/',
        default='image/img/default.png'
    )

    title = models.CharField(
        max_length=128,
        blank=False,
        null=False
    )

    content = models.TextField(
        blank=False,
        null=False
    )

    category = models.IntegerField(
        blank=False,
        null=False
    )

    like = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )

    one_line_introduce = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )

    as_rule = models.CharField(
        max_length=4096,
        blank=False,
        null=False,
    )

    refund_rule = models.CharField(
        max_length=4096,
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
