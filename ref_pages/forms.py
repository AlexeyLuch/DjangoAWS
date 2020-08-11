from django import forms

from .models import Referer


class TopicForm(forms.ModelForm):
    class Meta:
        model = Referer
        fields = ["text", "public"]
        labels = {"text": "label", "public": "label for public"}