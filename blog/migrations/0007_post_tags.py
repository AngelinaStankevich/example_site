# Generated by Django 4.2.4 on 2023-09-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="blog.tag"),
        ),
    ]
