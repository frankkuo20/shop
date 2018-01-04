from django import forms

from store.models import Category, Item


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='名稱', required=True)

    class Meta:
        model = Category
        fields = ('name', )


class ItemForm(forms.ModelForm):
    name = forms.CharField(label='名稱')
    category = forms.ModelChoiceField(Category.objects.all(), label='類別')
    price = forms.IntegerField(label='價錢')

    class Meta:
        model = Item
        fields = ('name', 'category', 'price', )