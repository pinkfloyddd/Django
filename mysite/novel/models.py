from django.db import models

class novel_info(models.Model):
    name = models.CharField(max_length=100)
    writter = models.CharField(max_length=100)
    pub = models.CharField(max_length=1000)
    pub_date = models.CharField(max_length=1000)
    price = models.FloatField()
    rating = models.IntegerField()
    rating_nums = models.IntegerField()
