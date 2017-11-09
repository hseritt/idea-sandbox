"""Forms module for tasks app."""
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'due', 'end', 'importance',
        ]
