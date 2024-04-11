from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Profile, Book


@receiver(post_migrate)
def create_profiles_for_book_columns(sender, **kwargs):
    for field in Book._meta.fields:
        column_name = field.name
        Profile.objects.get_or_create(column_name=column_name)
