from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


    def __init__(self, arg):
        super(Todo, self).__init__()
        self.arg = arg
