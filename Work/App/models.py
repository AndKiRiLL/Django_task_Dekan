from django.db import models

class Item_Page1(models.Model):
    caption = models.TextField()
    price = models.CharField(max_length=35)
    path_img = models.TextField()

class Item_Page2(models.Model):
    caption = models.TextField()
    price = models.CharField(max_length=35)
    path_img = models.TextField()

class Item_Page3(models.Model):
    caption = models.TextField()
    price = models.CharField(max_length=35)
    path_img = models.TextField()

