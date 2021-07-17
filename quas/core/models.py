from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
