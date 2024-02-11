from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(max_length=MAX_NAME_LENGTH, null=False, blank=False)
    pet_photo = models.URLField(null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

