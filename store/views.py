from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from store.forms import CategoryForm
from store.models import Category


def category(request):
    categorys = Category.objects.all()
    return render(request, 'store/category.html', {'categorys':categorys})


def categoryCreate(request):
    if request.method == 'GET':
        categoryForm = CategoryForm()
        return render(request, 'store/categoryCreate.html', {'categoryForm':categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST)
        if not categoryForm.is_valid():
            return render(request, 'store/categoryCreate.html', {'categoryForm':categoryForm})

        categoryForm.save()
        messages.success(request, '新增成功')
        messages.debug(request, 'debug')
        return redirect(reverse('store:category'))
