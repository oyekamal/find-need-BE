# Generated by Django 4.2.2 on 2024-04-23 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_imagegroup_index_alter_imagegroup_group_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='group_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.imagegroupname'),
        ),
    ]
