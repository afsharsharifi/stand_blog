from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    created = models.DateField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.filter(is_active=True))

    def get_active_items(self):
        return self.filter(is_active=True)


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="Categories")
    body = models.TextField(verbose_name="Content")
    image = models.ImageField(upload_to="images/articles", null=True, blank=True, verbose_name="Cover Image")
    slug = models.SlugField(blank=True, unique=True, verbose_name="Slug")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    publish_at = models.DateTimeField(null=True, verbose_name="Publish At")
    is_active = models.BooleanField(default=True, verbose_name="Activation")

    objects = ArticleManager()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" alt="{self.title}" width="45px">')
        return format_html("No Image")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(args, kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name="For")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="From")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies", verbose_name="Reply To")
    body = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Comment At")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.body
