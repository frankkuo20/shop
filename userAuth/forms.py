from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    email = forms.EmailField(label='信箱')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('密碼與確認密碼不同')
        return password2

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
