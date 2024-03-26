# Generated by Django 4.2.2 on 2024-03-26 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0025_extra_warranty_post_cylinders_post_doors_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegionSpecs",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="region_specs"),
                ),
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="region_specs",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="post.regionspecs",
            ),
        ),
    ]
