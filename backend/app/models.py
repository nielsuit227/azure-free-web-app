from django.db import models


class Object(models.Model):
    attribute = models.TextField()
