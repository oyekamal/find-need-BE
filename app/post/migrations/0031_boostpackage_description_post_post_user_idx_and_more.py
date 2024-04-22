# Generated by Django 4.2.2 on 2024-04-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0030_post_sold"),
    ]

    operations = [
        migrations.AddField(
            model_name="boostpackage",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["user"], name="post_user_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["city"], name="post_city_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["category"], name="post_category_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["sub_category"], name="post_sub_category_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["post_type"], name="post_post_type_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["year"], name="post_year_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["region"], name="post_region_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["region_specs"], name="post_region_specs_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["body_condition"], name="post_body_condition_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["mechanical_condition"], name="post_mechanical_condition_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["transmission"], name="post_transmission_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["fuel_type"], name="post_fuel_type_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["insurance"], name="post_insurance_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["payment_method"], name="post_payment_method_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["color"], name="post_color_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["warranty"], name="post_warranty_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["boost_score"], name="post_boost_score_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["view_count"], name="post_view_count_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["doors"], name="post_doors_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["cylinders"], name="post_cylinders_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["latitude", "longitude"], name="post_location_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["created_at"], name="post_created_at_idx"),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(fields=["updated_at"], name="post_updated_at_idx"),
        ),
    ]