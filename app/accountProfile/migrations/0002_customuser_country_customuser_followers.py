# Generated by Django 4.2.2 on 2023-09-25 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accountProfile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accountProfile.country",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="followers",
            field=models.ManyToManyField(
                related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
