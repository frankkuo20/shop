from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from userAuth.forms import RegisterForm


def userLogin(request):
    if request.method == 'GET':
        return render(request, 'userAuth/userLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, '請輸入帳號密碼')
            return render(request, 'userAuth/userLogin.html')

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, '登入失敗')
            return render(request, 'userAuth/userLogin.html')
        # user
        login(request, user)
        messages.error(request, '登入成功')
        return redirect(reverse('main:main'))


def userLogout(request):
    logout(request)
    messages.error(request, '登出成功')
    return redirect(reverse('main:main'))


def register(request):
    if request.method == 'GET':
        registerForm = RegisterForm()
        return render(request, 'userAuth/register.html', {'registerForm':registerForm})
    elif request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if not registerForm.is_valid():
            return render(request, 'userAuth/register.html', {'registerForm':registerForm})
        user = registerForm.save()
        user.set_password(user.password)
        user.save()
        messages.error(request, '註冊成功')
        return redirect(reverse('main:main'))