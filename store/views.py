from django.shortcuts import render

# Create your views here.
from store.models import Category


def category(request):
    categorys = Category.objects.all()
    return render(request, 'store/category.html', {'categorys':categorys})