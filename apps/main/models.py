from datetime import datetime, timezone
from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from auths.models import (
    CustomUser,
    Company,
    JobSeeker
)
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator,
    FileExtensionValidator,
    EmailValidator
)
from autoslug import AutoSlugField
from django.urls import reverse



class Language(models.Model):
    title = models.CharField(
        verbose_name='язык',
        max_length=100,
        unique=True
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        editable=True,
        verbose_name='Slug'
    )
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('language_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'язык'
        verbose_name_plural = 'языки'
        ordering = ('title',)


class CategoryChoices(models.Model):
        title = models.CharField(
            verbose_name ='категория',
            max_length=100,
            unique = True
        )
        slug = AutoSlugField(
        populate_from='title',
        unique=True,
        editable=True,
        verbose_name='слаг'
        )
        def __str__(self) -> Any:
            return self.title
        
        def get_absolute_url(self):
            return reverse('category_detail', kwargs={'slug': self.slug})
        
        class Meta:
            verbose_name= 'категория'
            verbose_name_plural = 'категории'
            ordering = ('-id',)


class CurriculumVitae(models.Model):
    """- Модель резюме"""

    

    class EmplymentStatusChoices(models.TextChoices):
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

    class CitizenChoices(models.TextChoices):
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

    class EducationChoices(models.TextChoices):
        MEDIUM= 'MDM',_('Среднее профессиональное образование')
        HIGH_BACHELOR = 'HBC',_('Высшее (бакалавриат)')
        HIGH_MAGISTR = 'HMG',_('Высшее (магистратура)')
        HIGH_PHD = 'HPH',_('Высшее (докторантура)')
        NONE = 'NON',_('Нет')

    class GenderChoices(models.TextChoices):
        NOT_SELECTED = 'N',_('Не выбрано')
        MAN = 'M',_("Мужской")
        WOMAN = 'W',_('Женский')


    class FamilyStatusChoices(models.TextChoices):
        NOT_SELECTED = 'N',_('Не выбрано')
        SINGLE = 'S',_('Не в браке')
        MARRIAGE ='M',_('В браке')
        MARRIAGE_AND_CHILDREN = 'MH',_('В браке (есть дети)')
        COUPLE = 'CP',_('В отношениях')


    class EducationFormChoices(models.TextChoices):
        FULL_TIME = 'FT',_('Очная')
        PART_TIME = 'PT',_('Очно-заочная')
        DISTANCE_LEARNING = 'DL',_('Заочная')

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
    birth_date = models.DateField(
        verbose_name='дата рождения',
        auto_now_add = True
    )
    employment_status = models.CharField(
        verbose_name='занятость',
        choices=EmplymentStatusChoices.choices,
        default=EmplymentStatusChoices.FULL,
        max_length=4
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to = CategoryChoices,
        on_delete = models.CASCADE,
        null = True,
        blank =True
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
        null=True,
        blank=True
    )
    citizenship = models.CharField(
        verbose_name='гражданство',
        choices=CitizenChoices.choices,
        default=CitizenChoices.NOT_SELECTED,
        max_length=3
    )
    living_place = models.CharField(
        verbose_name='город проживания',
        max_length=150,
        default='Караганда'
    )
    education = models.CharField(
        verbose_name='образование',
        max_length=3,
        choices=EducationChoices.choices,
        default=EducationChoices.NONE
    )
    gender = models.CharField(
        verbose_name='пол',
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.NOT_SELECTED
    )
    family_status = models.CharField(
        verbose_name='семейное положение',
        max_length=2,
        choices=FamilyStatusChoices.choices,
        default=FamilyStatusChoices.NOT_SELECTED
    )
    university = models.CharField(
        verbose_name='университет',
        max_length=255,
        null=True,
        blank=True
    )
    university_graduate_year = models.PositiveSmallIntegerField(
        verbose_name='год окончания',
        validators=[
            MinValueValidator(1970),
            MaxValueValidator(2030)
        ],
        default=2006
    )
    faculty = models.CharField(
        verbose_name='факультет',
        max_length=150,
        null=True,
        blank=True
    )
    speciality = models.CharField(
        verbose_name='специальность',
        max_length=150,
        null=True,
        blank=True
    )
    education_form = models.CharField(
        verbose_name='форма обучения',
        max_length=2,
        choices=EducationFormChoices.choices,
        default=EducationFormChoices.FULL_TIME
    )

    photo = models.ImageField(
        verbose_name='фото',
        upload_to=f'cv/',
        null=True,
        blank=True
    )
    coursess = models.TextField(
        verbose_name='курсы',
        null=True,
        blank=True,
        help_text='Напишите о курсах, которые проходили(необязательно)'
    )

    languages = models.ManyToManyField(
        verbose_name='владение языками',
        to=Language
    )

    @property
    def get_age(self):
        current_date = timezone.now()
        birth_year, birth_month, birth_day = self.birth_date.year, self.birth_date.month, self.birth_date.day
        current_year, current_month, current_day = current_date.year, current_date.month, current_date.day
        age = current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day))
        return age
    

    def __str__(self) -> str:
        return f'{self.user} | {self.title}'
    
    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        ordering = ('-id',)

    

class Vacancy(models.Model):

    class WorkExperienceChoices(models.TextChoices):
        NO_EXPERIENCE = 'NO',_('Без опыта')
        ONETOTHREE = '1-3',_('1-3 года')
        THREETOFIVE = '3-5',_('3-5 лет')
        FIVEANDMORE = '5-M',_('5 лет и больше')

    class SeleryTypeChoises(models.TextChoices):
        NETTO  = 'NETTO',_('Нетто')
        BRUTTO = 'BRUTTO',_('Брутто')

    company = models.ForeignKey(
        verbose_name='компания',
        to=CustomUser,
        related_name='vacancy',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='название вакансии',
        max_length=150
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to = CategoryChoices,
        on_delete = models.CASCADE,
        null = True,
        blank =True
    )
    selery_lower_limit = models.PositiveIntegerField(
        verbose_name = 'зарплата от',
        null= True,
        blank = True,
        help_text='введите нижний предел зарплаты'
    )
    selery_upper_limit = models.PositiveIntegerField(
        verbose_name = 'зарплата до',
        null = True,
        blank = True,
        help_text='введите верхний предел зарплаты'
    )
    selery_currency= models.CharField(
        verbose_name = 'валюта',
        max_length = 15,
        choices = CurriculumVitae.CurrencyChoices.choices,
        null = True,
        blank= True
    )
    selery_type = models.CharField(
        verbose_name = 'тип зарплаты',
        max_length= 15,
        choices = SeleryTypeChoises.choices,
        null = True,
        blank = True,
        help_text='выберите тип выплачиваемой зарплаты'
    )
    publish_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_created=True,
        default=datetime.now()
    )
    about_company = models.TextField(
        verbose_name='о компании',
        help_text='расскажите о вашей компании'
    )
    responsibilities = models.TextField(
        verbose_name='обязанности кандидата',
        help_text='расскажите об обязанностях кандидата'
    )
    specialization = models.TextField(
        verbose_name='специализация компании',
        help_text='расскажите о вашей специализации'
    )
    requirements = models.TextField(
        verbose_name='требования к кандидату',
        help_text='расскажите о требованиях к кандидату'
    )
    schedule = models.CharField(
        verbose_name='график работы',
        max_length=15,
        choices=CurriculumVitae.ScheduleChoices.choices,
        default=CurriculumVitae.ScheduleChoices.NOT_SELECTED
    )
    work_experience = models.CharField(
        verbose_name='опыт работы',
        max_length=5,
        choices=WorkExperienceChoices.choices,
        default=WorkExperienceChoices.ONETOTHREE
    )

    def __str__(self) -> str:
        return f'{self.company} | {self.title}'
    
    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        ordering = ('-id',)


class VacancyResponses(models.Model):

    user = models.ForeignKey(
        verbose_name = 'пользователь',
        to= CustomUser,
        on_delete = models.CASCADE,
        related_name = 'vacancy_responses'
    )
    vacancy = models.ForeignKey(
        verbose_name = 'вакансия',
        to= Vacancy,
        on_delete = models.CASCADE,
        related_name = 'responses'
    )
    cv = models.ForeignKey(
        verbose_name = 'резюме',
        to = CurriculumVitae,
        on_delete = models.CASCADE,
        related_name = 'responses'
    )
    datetime_response = models.DateTimeField(
        verbose_name = 'дата и время отклика',
        auto_now_add = True,
        null = True,
        blank = True
    )

    def __str__(self) -> str:
        return f'{self.user} откликнулся на вакансию: {self.vacancy} | Дата: {self.datetime_response}'
    class Meta:
        verbose_name = 'отклик на вакансию'
        verbose_name_plural = 'отклики на вакансию'
        ordering = ('-id',)
