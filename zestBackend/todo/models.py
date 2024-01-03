from django.db import models


class TodoItem(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    due_date = models.DateField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
