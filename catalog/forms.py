from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа',
                            'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Название содержит запрещённые слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in ['казино', 'криптовалюта', 'крипта', 'биржа',
                            'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Описание содержит запрещённые слова')

        return cleaned_data
