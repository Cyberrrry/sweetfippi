
from django.db import models
from django import forms


class Product(models.Model):
    id = models.AutoField(primary_key=True,)
    pr_img1 = models.ImageField(upload_to="polls/images", default="")
    pr_img2 = models.ImageField(upload_to="polls/images", default="")
    pr_img3 = models.ImageField(upload_to="polls/images", default="")
    pr_img4 = models.ImageField(upload_to="polls/images", default="")
    pr_img5 = models.ImageField(upload_to="polls/images", default="")
    pr_rv1 = models.ImageField(upload_to="polls/images", default="")
    pr_rv2 = models.ImageField(upload_to="polls/images", default="")
    pr_rv3 = models.ImageField(upload_to="polls/images", default="")
    pr_rv4 = models.ImageField(upload_to="polls/images", default="")
    pr_rv5 = models.ImageField(upload_to="polls/images", default="")
    product_name = models.CharField(max_length=500)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    off = models.CharField(max_length=80, default=0)
    desc = models.CharField(max_length=900)
    out_of_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Upi(models.Model):
    upi = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.upi
