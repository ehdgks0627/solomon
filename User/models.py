from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)


class AccountManager(BaseUserManager):
    # TODO add tuhmbnail field
    def create_account(self, id, password, email, nickname, phone):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            id=id,
            email=AccountManager.normalize_email(email),
            nickname=nickname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password, email, nickname, phone):
        user = self.create_account(
            id=id,
            password=password,
            email=email,
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
    nickname = models.CharField(
        'nickname',
        max_length=10,
        blank=False,
        unique=True,
        default='')
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='image/thumbnail/',
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
    REQUIRED_FIELDS = ['nickname', 'email', 'phone']

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
