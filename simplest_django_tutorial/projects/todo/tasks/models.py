"""Models module for the tasks app."""
from django.db import models


class Task(models.Model):

    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    end = models.DateTimeField()
    importance = models.CharField(
        'Importance', max_length=50, choices=(
            ('Important/Urgent', 'Important/Urgent'),
            ('Important/Not urgent', 'Important/Not urgent'),
            ('Not important/Urgent', 'Not important/Urgent'),
            ('Not important/Not urgent', 'Not important/Not urgent'),
        )
    )

    def __str__(self):
        return self.title