from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)


class AccountManager(BaseUserManager):
    # TODO add tuhmbnail field
    def create_user(self, id, password, email, name, nickname, phone):
        user = self.model(
            id=id,
            email=AccountManager.normalize_email(email),
            name=name,
            nickname=nickname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password, email, name, nickname, phone):
        user = self.create_user(
            id=id,
            password=password,
            email=email,
            name=name,
            nickname=nickname,
            phone=phone
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        verbose_name='id',
        primary_key=True,
        max_length=32,
        unique=True,
        null=False,
        blank=False
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    name = models.CharField(
        verbose_name='name',
        max_length=32,
        blank=False,
        unique=False
    )

    nickname = models.CharField(
        verbose_name='nickname',
        max_length=16,
        blank=False,
        unique=True,
        default=''
    )

    thumbnail = models.ImageField(
        verbose_name='thumbnail',
        null=True,
        blank=True,
        upload_to='static/files/img/',
    )

    phone = models.CharField(
        verbose_name='phone',
        max_length=16,
        unique=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'nickname', 'email', 'phone']

    @property
    def is_staff(self):
        return self.is_superuser
