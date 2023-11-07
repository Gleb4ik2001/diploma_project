from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
    User
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    def _create_user(self, email,password, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError('Логин обязателен')
        email =self.normalize_email(email)
        user :User= self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self, email, password, **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)
       

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='почта',
        unique=True
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
    birth_date = models.DateField(
        verbose_name='дата рождения',
        null=True,
        blank=True
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

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-id',)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    

class CurriculumVitae(models.Model):

    class Category(models.TextChoices):
        NOT_SELECTED = 'NOT_SELECTED',_('Не выбрано')
        IT = 'IT',_('Информаионные технологии')
        HEALTH = 'HEALTH',_('Здравохранение')
        EDUCATION = 'EDUCATION',_('Образование')
        MANUFACTURING = 'MANUFACTURING',_('Производство и инженерия')
        FINANCES = 'FINANCES',_('Финансы')
        MARKETING = 'MARKETING',_('Маркетинг и реклама')
        HOTEL = 'HOTEL',_('Гостиничный бизнес')
        RESTAURANT = 'RESTAURANT',_('Ресторанный бизнес')
        SALES = 'SALES',_('Продажи')
        ART = 'ART',_('Искусство')
        FUN = 'FUN',_('Развлечения')
        TRANSPORT = 'TRANSPORT',_('Транспорт и логистика')
        BUILDING = 'BUILDING',_('Строительство и архитектура')
        AGRICULTURE = 'AGRICULTURE',_('Сельское хозяйство и сельскохозяйственные науки')
        UNCOMMERCIAL = 'UNCOMMERCIAL',_('Некоммерческий сектор')
        JURISPRUDENCE = 'JURISPRUDENCE',_('Юриспруденция и право')
        SPORT = 'SPORT',_('Спорт и физическая активность')
    user = models.ForeignKey(
        verbose_name='пользователь',
        to=CustomUser,
        on_delete=models.PROTECT,
        related_name='cv',
    )
    title = models.CharField(
        verbose_name='название профессии',
        max_length=255,
        null=True,
        blank=True
    )
    category = models.CharField(
        max_length=100,
        choices=Category.choices,
        default=Category.NOT_SELECTED
    )
    photo = models.ImageField(
        verbose_name='фото',
        upload_to=f'cv/',
        null=True,
        blank=True
    )   
    def __str__(self) -> str:
        return f'{self.user} | {self.title}'
    
    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        ordering = ('-id',)

    


