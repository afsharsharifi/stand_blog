# Generated by Django 4.1 on 2022-09-11 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0016_article_publish_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "Comment", "verbose_name_plural": "Comments"},
        ),
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="body",
            field=models.TextField(verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ManyToManyField(
                related_name="articles", to="blog.category", verbose_name="Categories"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/articles",
                verbose_name="Cover Image",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Activation"),
        ),
        migrations.AlterField(
            model_name="article",
            name="publish_at",
            field=models.DateTimeField(null=True, verbose_name="Publish At"),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(blank=True, unique=True, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated At"),
        ),
        migrations.AlterField(
            model_name="category",
            name="created",
            field=models.DateField(auto_now_add=True, verbose_name="Created At"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.article",
                verbose_name="For",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(verbose_name="Comment"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Comment At"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="blog.comment",
                verbose_name="Reply To",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="From",
            ),
        ),
    ]
