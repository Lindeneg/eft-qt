from django.db import models

from jsonfield import JSONField


class Item(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    url = models.URLField(max_length=200)
    item_type = models.CharField(max_length=120)
    img_info = JSONField(null=True)
    notes = JSONField(null=True)

    def __str__(self):
        return self.name