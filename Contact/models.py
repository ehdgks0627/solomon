from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)


class ContactManager(BaseUserManager):
    def create_post(self, type, orderId, nickname, email, title, main, file):

        post = self.model(
            type=type,
            orderId=orderId,
            nickname=nickname,
            email=ContactManager.normalize_email(email),
            title=title,
            main=main,
            file=file,
        )

        post.save(using=self._db)
        return post


class ContactPost(AbstractBaseUser, PermissionsMixin):
    SELLER = 'sr'
    BUYER = 'br'
    TYPE_CHOICES = (
        (SELLER, '판매자'),
        (BUYER, '구매자'),
    )

    type = models.CharField(
        verbose_name='type',
        max_length=2,
        choices=TYPE_CHOICES,
        default=SELLER
    )
    orderId = models.CharField(
        verbose_name='id',
        primary_key=True,
        max_length=32,
        unique=True,
        null=False,
        blank=False
    )
    nickname = models.CharField(
        verbose_name='nickname',
        max_length=10,
        blank=False,
        unique=True,
        default=''
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    title = models.CharField(
        verbose_name='title',
        max_length=100,
        unique=True,
        default=''
    )
    main = models.CharField(
        verbose_name='main',
        max_length=1000,
        unique=True,
        default=''
    )
    file = models.FileField(
        upload_to='image/contact/'
    )

    is_active = models.BooleanField(default=True)

    objects = ContactManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['type', 'orderId', 'nickname', 'email', 'title', 'main']