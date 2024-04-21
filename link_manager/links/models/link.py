from django.db import models
from .user import CustomUser
from .collection import Collection


class Link(models.Model):
    TITLE_MAX_LENGTH = 255
    DESCRIPTION_MAX_LENGTH = 512

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, blank=True, null=True)
    url = models.URLField()
    image = models.URLField(blank=True, null=True)
    LINK_TYPE_CHOICES = [
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    ]
    link_type = models.CharField(max_length=10, choices=LINK_TYPE_CHOICES, default='website')
    collections = models.ManyToManyField(Collection, related_name='links')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
