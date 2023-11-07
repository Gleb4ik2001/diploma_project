from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import(
    MinValueValidator
)

class CustomUserManager(UserManager):
    def _create_user(self, email,password, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError('Логин обязателен')
        email =self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
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

    class EmplymentStatus(models.TextChoices):
        NOT_SELECTED = 'NSL',_('Не выбрано')
        FULL = 'FULL',_('Полная занятость')
        PART = 'PART',_('Частичная занятость')
        VOLUNTEERING = 'VLNT',_('Волонтерство')

    class YesOrNoChoices(models.TextChoices):
        NOT_SELECTED = 'NSL',_('Не выбрано')
        YES = 'YES',_('Да')
        NO = 'NO',_('Нет')

    class ScheduleChoices(models.TextChoices):
        NOT_SELECTED = 'NOTSELECTED',_('Не выбрано')
        FULL_DAY = 'FULL_DAY',_('Полный день')
        FLEX = 'FLEX',_('Гибкий формат')
        TWOXTWO = '2x2',_('2/2')
        HALF_TIME = 'HALFTIME',_('Половина ставки')
        REMOTE = 'REMOTE',_('Удаленная работа')
        HYBRID = 'HYBRID',_('Гибридный формат')

    class CurrencyChoices(models.TextChoices):
        NOT_SELECTED = 'NOTSELECTED',_('Не выбрано')
        KZT = 'KZT',_('Тенге')
        RUB = 'RUB',_('Рубли')
        USD = 'USD',_('Доллары')
        EUR = 'EUR',_('Евро')
        CAD = 'CAD',_('Канадский доллар')
        GBP = 'GBP',_('Британский фунт')
        CNH = 'CNH',_('Китайский юань')

    class CitizenChoises(models.TextChoices):
        NOT_SELECTED = 'NTS',_('Не выбрано')
        KAZAKHSTAN = 'KZ',_('Казахстан')
        RUSSIA = 'RU',_('Российская Федерация')
        BELARUS = 'BEL',_('Беларусь')
        UKRAINE = 'UA',_('Украина')
        UZBEKISTAN = 'UZB',_('Узбекистан')
        GRUZIA = 'GRX',_('Грузия')
        CHINA = 'CHN',_('Китай')
        AZERBAIJAN = 'AZB',_('Азербайджан')
        ARMENIA = 'ARM',_('Армения')
        KYRGYZSTAN = 'KRG',_('Кыргызстан')
        USA = 'USA',_('Соединенные Штаты Америки')
        CANADA = 'CND',_('Канада')
        POLAND = 'PL',_('Польша')
        CHECH_REPUBLIC = 'CZR',_('Чехия')
        GREECE = 'GRC',_('Греция')
        GERMANY = 'GRM',_('Германия')
        ITALY = 'ITL',_('Италия')
        GREAT_BRITAIN = 'GBT',_('Великобритания')
        FRANCE = 'FRN',_('Франция')
        SWEDEN = 'SWD',_('Швеция')
        SWITZERLAND = 'SWZ',_('Швейцария')
        NETHERLANDS = 'NTL',_('Нидерланды')

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
    employment_status = models.CharField(
        verbose_name='занятость',
        choices=EmplymentStatus.choices,
        default=EmplymentStatus.FULL,
        max_length=4
    )
    category = models.CharField(
        verbose_name='категория',
        max_length=100,
        choices=Category.choices,
        default=Category.NOT_SELECTED,
    )
    business_trip_readiness = models.CharField(
        verbose_name='готовность к командировкам',
        choices=YesOrNoChoices.choices,
        default=YesOrNoChoices.NOT_SELECTED,
        max_length=3
    )
    schedule = models.CharField(
        verbose_name='график работы',
        choices=ScheduleChoices.choices,
        default=ScheduleChoices.NOT_SELECTED,
        max_length=12
    )
    desired_salary = models.PositiveIntegerField(
        verbose_name='желаемая зарплата',
        default=100
    )
    currency = models.CharField(
        verbose_name='валюта',
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.NOT_SELECTED,
        max_length=12
    )
    phone_number = models.CharField(
        verbose_name='номер телефона',
        max_length=100,
        default=None
    )
    job_email = models.EmailField(
        verbose_name='почта для связи',
        unique=True,
        null=True,
        blank=True
    )
    citizenship = models.CharField(
        verbose_name='гражданство',
        choices=CitizenChoises.choices,
        default=CitizenChoises.NOT_SELECTED,
        max_length=3
    )
    living_place = models.CharField(
        verbose_name='город проживания',
        max_length=150,
        default='Караганда'
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

    


