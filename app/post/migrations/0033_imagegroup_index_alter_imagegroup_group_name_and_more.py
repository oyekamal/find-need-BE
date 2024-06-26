# Generated by Django 4.2.2 on 2024-04-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0032_imagegroupname_postexampleimage_imagegroup"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagegroup",
            name="index",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="imagegroup",
            name="group_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.imagegroupname"
            ),
        ),
        migrations.AlterField(
            model_name="imagegroup",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.postexampleimage"
            ),
        ),
    ]
