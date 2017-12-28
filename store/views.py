from django.shortcuts import render, redirect

# Create your views here.
from store.models import Category


def category(request):
    categorys = Category.objects.all()
    return render(request, 'store/category.html', {'categorys':categorys})

def categoryCreate(request):
    if request.method == 'GET':
        return render(request, 'store/categoryCreate.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        category = Category()
        category.name = name
        category.save()
        return redirect('/store/category')
