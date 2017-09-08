from random import randint

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


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
            while True:
                random_number = randint(10**2, 10**10 - 1)
                raw_slug = '{}-{}'.format(self.title, random_number)
                self.slug = slugify(raw_slug, allow_unicode=True)
                if not Entry.objects.filter(slug=self.slug).exists():
                    break
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('entry_detail', kwargs=kwargs)
