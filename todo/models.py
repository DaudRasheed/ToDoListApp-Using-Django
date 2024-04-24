from django.db import models

# Create your models here.
# The `Todo` class defines a model with a `title` field of type `CharField` in Django.
class Todo(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) :
        
        
        return self.title
