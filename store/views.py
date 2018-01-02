from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

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
        return redirect(reverse('store:category'))


def categoryUpdate(request, id):
    category = get_object_or_404(Category, id=id)
    # category = Category.objects.get(id=id)
    if request.method == 'GET':
        categoryForm = CategoryForm(instance=category)
        return render(request, 'store/categoryUpdate.html', {'categoryForm': categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST, instance=category)
        if not categoryForm.is_valid():
            return render(request, 'store/categoryUpdate.html', {'categoryForm':categoryForm})

        categoryForm.save()
        messages.success(request, '修改成功')
        return redirect(reverse('store:category'))

