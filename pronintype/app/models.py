from django.db import models

# Create your models here.

class Level(models.Model):
    title = models.CharField(max_length=100)


class Words(models.Model):
    level_id = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    word = models.CharField(max_length=100)