# Generated by Django 4.2.2 on 2023-10-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "accountProfile",
            "0005_alter_customuser_country_alter_customuser_followers_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="language",
            old_name="flag_pictures",
            new_name="image",
        ),
        migrations.AddField(
            model_name="city",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="flag_pictures"),
        ),
        migrations.AddField(
            model_name="country",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="flag_pictures"),
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=150),
        ),
    ]
