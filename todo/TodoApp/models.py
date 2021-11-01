from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    desc   = models.TextField(max_length=150)
    date   = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2 , choices=status_choices)

  
