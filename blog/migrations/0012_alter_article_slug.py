# Generated by Django 4.1 on 2022-08-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
