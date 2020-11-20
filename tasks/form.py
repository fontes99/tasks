from rest_framework.serializers import ModelSerializer

from .models import Task
from django import forms

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'pub_date', 'description')
