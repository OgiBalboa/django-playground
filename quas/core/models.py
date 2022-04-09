from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=350, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)
    extra_fields = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True
