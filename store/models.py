import random

from django.db import models
from django.contrib.auth.models import User


def create_new_ref_number():
    return int(random.randint(1000000000, 9999999999))


# class Isbn(models.Model):
#     isbn_number = models.CharField(max_length=10, unique=True, default=create_new_ref_number())
#     title = models.CharField(max_length=10)
#     author = models.CharField(max_length=50)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Metric(models.Model):
    visits = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    ratio = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.visits} Visits | {self.likes} likes | {self.ratio} ratio"


class Store(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="books")
    content = models.TextField(max_length=2048, null=True, blank=True)
    isbn_number = models.CharField(max_length=10, unique=True, default=create_new_ref_number())
    # Isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category)
    metrics = models.ForeignKey(Metric, on_delete=models.CASCADE, null=True, blank=True)
    thumb = models.ImageField(upload_to='books')

    def __str__(self):
        return self.title
