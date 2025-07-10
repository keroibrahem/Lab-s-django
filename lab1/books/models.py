from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError("Category name must be at least 2 characters.")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def clean(self):
        if len(self.title) < 10 or len(self.title) > 50:
            raise ValidationError("Book title must be between 10 and 50 characters.")

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    number = models.CharField(max_length=13, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.number:
            import uuid
            self.number = str(uuid.uuid4().int)[:13]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book_title} - {self.number}"
