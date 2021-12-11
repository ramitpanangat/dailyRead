from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author.first_name} {self.author.last_name} | {self.category}"