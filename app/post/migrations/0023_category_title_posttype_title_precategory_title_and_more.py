# Generated by Django 4.2.2 on 2024-02-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0022_reportchat_audio_reportchat_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="posttype",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="precategory",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
