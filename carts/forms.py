from django import forms
from . import models


class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = models.Address
        fields = "__all__"
