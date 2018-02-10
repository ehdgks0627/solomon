from django.db import models
from user.models import Account


class Category:
    CATEGORY_CHOICES = [
        ({'kor': u'소프트웨어 개발', 'eng': 'Software Development'}, [
            (101, {'kor': u'웹사이트', 'eng': 'Web'}),
            (102, {'kor': u'안드로이드앱', 'eng': 'AndroidApp'}),
            (103, {'kor': u'아이폰', 'eng': 'IOS'}),
            (104, {'kor': u'응용프로그래밍', 'eng': 'Application'}),
            (105, {'kor': u'기술지원 / 원격', 'eng': 'Support / Remote'}),
            (106, {'kor': u'임베디드', 'eng': 'Embedded'}),
            (107, {'kor': u'매크로', 'eng': 'Macro'}),
            (108, {'kor': u'PC견적', 'eng': 'PC'}),
            (109, {'kor': u'IoT', 'eng': 'IoT'}),
            (110, {'kor': u'게임', 'eng': 'Game'}),
            (111, {'kor': u'기타', 'eng': 'Etc'}),
        ]),
        ({'kor': u'디자인', 'eng': 'Design'}, [
            (201, {'kor': u'웹디자인', 'eng': 'Web'}),
            (202, {'kor': u'로고 / CI&BI', 'eng': 'Logo / CI&BI'}),
            (203, {'kor': u'캘리그라피', 'eng': 'Calligraphy'}),
            (204, {'kor': u'전단지 / 홍보물', 'eng': 'Web'}),
            (205, {'kor': u'명함', 'eng': 'Business Card'}),
            (206, {'kor': u'일러스트', 'eng': 'Illustration'}),
            (207, {'kor': u'캐리커쳐', 'eng': 'Caricature'}),
            (208, {'kor': u'만화 / 웹툰', 'eng': 'Web'}),
            (209, {'kor': u'캐릭터 / 아이콘', 'eng': 'Icon'}),
            (210, {'kor': u'패키지', 'eng': 'Package Design'}),
            (211, {'kor': u'인테리어', 'eng': 'Interior'}),
            (222, {'kor': u'3D', 'eng': '3D'}),
            (223, {'kor': u'PPT', 'eng': 'PPT'}),
            (224, {'kor': u'포토샵', 'eng': 'Photoshop'}),
            (225, {'kor': u'사진촬영', 'eng': 'Take a Photo'}),
            (226, {'kor': u'누끼작업', 'eng': ''}),
            (227, {'kor': u'기타', 'eng': 'Etc'}),
        ])
    ]

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
        upload_to='static/files/img/',
        default='static/files/img/default.png'
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
