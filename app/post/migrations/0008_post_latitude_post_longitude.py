# Generated by Django 4.2.2 on 2023-09-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0007_boostpackage_post_boost_score_post_expiration_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
