from django import forms
from car_app.models import Car
from django.forms import formset_factory


class CarForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Car
        fields = "__all__"


CarFormSet = formset_factory(CarForm, extra=0)
