from typing import Any
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
    BaseUserManager
)
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator,
    FileExtensionValidator,
    EmailValidator
)
from datetime import(
    datetime,
    timedelta
)
from django.utils import timezone
from django.core import signing

class CustomUserManager(BaseUserManager):
    """- Менеджер объектов пользователя"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_jobseeker(self,email,password = None,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_company=False,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_company(self,email,password = None,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_company=True,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.all()
       

class CustomUser(AbstractBaseUser,PermissionsMixin):
    """Модель пользователя"""

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
        validators=[EmailValidator("Введите корректный адрес электронной почты.")]
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=100,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150,
        null=True,
        blank=True
    )
    company_name = models.CharField(
        verbose_name='название компании',
        max_length=100,
        null=True,
        blank=True
    )
    birth_date = models.DateField(
        verbose_name='дата рождения',
        null=True,
        blank=True
    )
    photo = models.ImageField(
        verbose_name='фото/логотип',
        upload_to='logos/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                ['PNG', 'JPEG', 'GIF', 'RAW', 'TIFF', 'BMP', 'PSD','JPG'],
                'Формат загруженного файла не поддерживается'
            )
        ]
    )
    is_company = models.BooleanField(
        verbose_name = 'компания',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='статус активности',
        default=True
    )
    is_superuser=models.BooleanField(
        verbose_name='статус администратора',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='статус работника',
        default=False
    )
    datetime_joined = models.DateTimeField(
        verbose_name='дата регистрации',
        default=timezone.now
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-id',)


class JobSeekerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        result = super().get_queryset(*args, **kwargs)
        return result.filter(is_company= False)
    
class JobSeeker(CustomUser):
    jobseekers = JobSeekerManager()

    class Meta:
        proxy =True
        verbose_name = 'соискатель'
        verbose_name_plural = 'соискатели'
        ordering = ('-id',)



class CompanyManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs) -> QuerySet:
        result = super().get_queryset(*args,**kwargs)
        return result.filter(is_company = True)

class Company(CustomUser):

    companys = CompanyManager()
    class Meta:
        proxy =True
        verbose_name = 'компания'
        verbose_name_plural = 'компания'
        ordering = ('-id',)