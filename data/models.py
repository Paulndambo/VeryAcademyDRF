from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Club(models.Model):
  name = models.CharField(max_length=200)
  money = models.FloatField(default=0)

  def __str__(self):
    return self.name

  def slice_money(self):
    return self.money

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    choices = (
        ('draft', 'Draft'), ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=20, choices=choices, default='published')
    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager

    class Meta:
        ordering = ['-published',]

    def __str__(self):
        return self.title