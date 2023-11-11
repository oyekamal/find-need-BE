# Generated by Django 4.2.2 on 2023-10-26 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountProfile', '0004_city_created_at_city_updated_at_country_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountProfile.country'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='accountProfile.language'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]