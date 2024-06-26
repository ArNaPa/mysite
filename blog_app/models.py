from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category (models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):     # Method for class return a name, not an object
        return self.category_name


STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published")
)


class Blog (models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    featured_image = models.ImageField(upload_to='static/uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=2000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

