from django import forms
from main.models import CurriculumVitae,Vacancy

class JobSeekerRegistrationForm(forms.Form):
    email = forms.EmailField(label='Email адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email адрес',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['company']  

class CurriculumVitaeForm(forms.ModelForm):
    class Meta:
        model = CurriculumVitae
        exclude = ['user']  # Пользователь будет установлен автоматически в представлении