from django import forms
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from django.core.validators import MinValueValidator, MaxValueValidator


class EmailContactForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    subject = forms.CharField(max_length=25, label='', widget=forms.TextInput(attrs={'placeholder': _('Subject')}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Message'), 'rows': '2'}), label='', required=True)
    captcha = CaptchaField()


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=25, label=_('First Name'), required=True)
    last_name = forms.CharField(max_length=25, label=_('Last Name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'placeholder': "name@example.com"}))
    phone = forms.CharField(max_length=15, label=_('Phone'), required=True)
    address = forms.CharField(max_length=100, label=_('Address'), required=True)
    age = forms.IntegerField (label=_("Age"), required=True, min_value=18, max_value=65)
    vacancy = forms.CharField(label=_("Vacancy"), max_length=30, required=True)
    experience = forms.CharField(label=_("Experience"), max_length=20, required=True)
    qualification = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Describe your qualification'), 'rows': '3'}), label=_("Qualification"), required=True)
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'placeholder': _('Message'), 'rows': '3'}))
    captcha = CaptchaField()