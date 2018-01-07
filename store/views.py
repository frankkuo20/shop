from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from store.forms import CategoryForm, ItemForm
from store.models import Category, Item


def category(request):
    categorys = Category.objects.all()
    return render(request, 'store/category.html', {'categorys': categorys})


def categoryRead(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'store/categoryRead.html', {'category': category})


def categoryCreate(request):
    if request.method == 'GET':
        categoryForm = CategoryForm()
        return render(request, 'store/categoryCreate.html', {'categoryForm': categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST)
        if not categoryForm.is_valid():
            return render(request, 'store/categoryCreate.html', {'categoryForm': categoryForm})

        categoryForm.save()
        messages.success(request, '新增成功')
        return redirect(reverse('store:category'))


def categoryUpdate(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        categoryForm = CategoryForm(instance=category)
        return render(request, 'store/categoryUpdate.html', {'categoryForm': categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST, instance=category)
        if not categoryForm.is_valid():
            return render(request, 'store/categoryUpdate.html', {'categoryForm': categoryForm})

        categoryForm.save()
        messages.success(request, '修改成功')
        return redirect(reverse('store:category'))


def categoryDelete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, '刪除成功')
    return redirect(reverse('store:category'))


def itemCreate(request):
    if request.method == 'GET':
        itemForm = ItemForm()
        return render(request, 'store/itemCreate.html', {'itemForm': itemForm})
    elif request.method == 'POST':
        itemForm = ItemForm(request.POST)
        if not itemForm.is_valid():
            return render(request, 'store/itemCreate.html', {'itemForm': itemForm})

        itemForm.save()
        messages.success(request, '新增成功')
        return redirect(reverse('store:category'))

def itemRead(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'store/itemRead.html', {'item': item})