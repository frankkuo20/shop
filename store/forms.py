from django import forms

from store.models import Category, Item


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='名稱', required=True)

    class Meta:
        model = Category
        fields = ('name', )


class ItemForm(forms.ModelForm):
    name = forms.CharField(label='名稱', widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(Category.objects.all(), label='類別', widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(label='細節', widget=forms.Textarea(attrs={'class': 'tinymceTextarea'}))
    price = forms.IntegerField(label='價錢', widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Item
        fields = ('name', 'category', 'description', 'price', )