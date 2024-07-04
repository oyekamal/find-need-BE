# Generated by Django 4.2.2 on 2024-07-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accountProfile", "0012_remove_customuser_languages_customuser_languages"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chatmessage",
            options={"ordering": ["-timestamp"]},
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="normal_chat/file"),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="normal_chat"),
        ),
    ]
