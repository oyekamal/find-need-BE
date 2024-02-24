# Generated by Django 4.2.2 on 2024-02-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0020_reportchat"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "PENDING"),
                    ("blocked", "BLOCKED"),
                    ("resolved", "RESOLVED"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
