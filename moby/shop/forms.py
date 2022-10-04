from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserCheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class BuyerAccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tel'].required = True
        self.fields['address'].required = True
        self.fields['name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = Buyer
        fields = ['name', 'email', 'tel', 'address']


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_text'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 80})

    class Meta:
        model = Review
        fields = ['grade', 'review_text', 'product', 'review_author']


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].widget = forms.HiddenInput()
        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Sale
        fields = ['order', 'region', 'city', 'department']
        required = (
            'region',
            'city',
            'department',
        )


class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label=_('Имя'))
    email = forms.EmailField(required=True, label=_('Почта'))
    tel = forms.CharField(max_length=15, min_length=8, required=True, label=_('Телефон'))
    address = forms.CharField(max_length=30, required=True, label=_('Адресс'))
    order = forms.ModelChoiceField(required=False, queryset=Order.objects.all(), widget=forms.HiddenInput())
    region = forms.CharField(max_length=80, required=True, label=_('Область'))
    city = forms.CharField(max_length=80, required=True, label=_('Город'))
    department = forms.CharField(max_length=8, required=True, label=_('Отделение'))


class BrandFilterForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'] = forms.MultipleChoiceField(choices=choices,
                                                         widget=forms.CheckboxSelectMultiple,
                                                         label=_('Бренд'))


class PriceFilterForm(forms.Form):
    low = forms.DecimalField(
        label=_('От'),
        required=False,
        widget=forms.NumberInput(attrs={'style': 'width:70px; margin-right:5px'}))
    high = forms.DecimalField(label=_('До'), required=False, widget=forms.NumberInput(attrs={'style': 'width:70px'}))
