from django.db import models


class Url(models.Model):
    url = models.URLField()
    upa = models.FloatField(default=0)
    pda = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
