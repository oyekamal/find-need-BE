# Generated by Django 4.2.2 on 2023-12-20 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "accountProfile",
            "0006_rename_flag_pictures_language_image_city_image_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="followers",
        ),
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "follower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "following",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
