from django.db import models

class Helpus(models.Model):
    titles = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.titles

class Category(models.Model):
    name = models.CharField(max_length=200)
