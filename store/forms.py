from django import forms
from .models import Store
from django.core.exceptions import ValidationError


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"
        exclude = ("isbn",)

    def clean(self):
        super(StoreForm, self).clean()
        content = self.cleaned_data.get("content")
        title = self.cleaned_data.get("title")
        if len(content) < 2:
            raise ValidationError("content must be bigger than 2 chars")

        if len(title) < 2:
            raise ValidationError("Title must be bigger than 2 chars")

        return self.cleaned_data
