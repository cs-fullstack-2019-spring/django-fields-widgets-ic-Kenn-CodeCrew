from django import forms
from .models import Application


levelOfProgramming = (
    (0, 'Terrible'),
    (1, 'Not that good'),
    (2, 'Just okay'),
    (3, 'Good'),
    (4, 'Pro'),
    (5, 'I only speak in javaScript'),
)


FRUIT_CHOICES= (
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {
            "date": forms.SelectDateWidget(),
            # "dropDown": forms.Select(choices=[("yes", "Yes"), ("no", "No")]),
            "dropDown": forms.SelectMultiple(choices=FRUIT_CHOICES),
            "radio": forms.RadioSelect(choices=FRUIT_CHOICES),
            "checkbox": forms.CheckboxSelectMultiple(choices=FRUIT_CHOICES),
        }