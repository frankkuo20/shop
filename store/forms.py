from django import forms

from store.models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='類別', required=True)

    class Meta:
        model = Category
        fields = ('name', )