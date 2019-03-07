from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(),
            "date": forms.SelectDateWidget(years=(1980, 2020)),
        }
