from django.db import models


class ShortUrl(models.Model):
    complete_url = models.URLField(unique=True, db_index=True, )
    short_url = models.URLField()
