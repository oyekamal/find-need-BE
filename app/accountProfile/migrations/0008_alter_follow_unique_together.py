# Generated by Django 4.2.2 on 2024-04-15 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountProfile', '0007_remove_customuser_followers_follow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
    ]