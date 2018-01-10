from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def userLogin(request):
    if request.method == 'GET':
        return render(request, 'auth/userLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, '請輸入帳號密碼')
            return render(request, 'auth/userLogin.html')

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, '登入失敗')
            return render(request, 'auth/userLogin.html')
        # user
        login(request, user)
        messages.error(request, '登入成功')
        return redirect(reverse('main:main'))


def userLogout(request):
    logout(request)
    messages.error(request, '登出成功')
    return redirect(reverse('main:main'))
