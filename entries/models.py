from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from .utils import generate_slug


class Entry(models.Model):
    title = models.CharField(max_length=96)
    signature = models.CharField(max_length=64)
    text = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    session_key = models.CharField(max_length=40)  # see https://docs.djangoproject.com/en/1.11/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.session_key
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(
                model=Entry,
                slug_prefix=self.title
            )
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('entry_detail', kwargs=kwargs)
