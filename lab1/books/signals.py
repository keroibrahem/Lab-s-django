from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book, ISBN

@receiver(pre_save, sender=Book)
def create_isbn(sender, instance, **kwargs):
    if not instance.isbn_id:
        isbn = ISBN(author="Unknown", book_title=instance.title)
        isbn.save()
        instance.isbn = isbn
