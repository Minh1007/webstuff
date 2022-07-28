from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

class tbl_user(AbstractUser):
    image = models.ImageField(null=False, upload_to="static/library/img/user")


class Category(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, null=False, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, null=False, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Content(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, null=False, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=False, null=False)
    rating = models.FloatField(blank=False, null=False)
    site_url = models.CharField(max_length=255, blank=False, null=False)
    staff_comment = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(null=False, upload_to="static/library/img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False)
    admin = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=False)
