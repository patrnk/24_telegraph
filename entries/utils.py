from random import randint

from django.utils.text import slugify


def generate_slug(model, slug_prefix=''):
    while True:
        random_number = randint(10**2, 10**10 - 1)
        raw_slug = '{}-{}'.format(slug_prefix, random_number)
        slug = slugify(raw_slug, allow_unicode=True)
        if not model.objects.filter(slug=slug).exists():
            break
    return slug
