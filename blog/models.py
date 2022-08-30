from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.filter(is_active=True))

    def get_active_items(self):
        return self.filter(is_active=True)


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"id": self.pk})

    def save(self, *args, **kwargs):
        self.title = self.title.replace(" ", "-")
        super(Article, self).save(args, kwargs)
