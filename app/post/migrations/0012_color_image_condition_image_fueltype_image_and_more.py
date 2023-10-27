# Generated by Django 4.2.2 on 2023-10-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_condition_fueltype_insurance_paymentmethod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='color'),
        ),
        migrations.AddField(
            model_name='condition',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='condition'),
        ),
        migrations.AddField(
            model_name='fueltype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fuel_type'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='insurance'),
        ),
        migrations.AddField(
            model_name='option',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='option'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='payment_method'),
        ),
        migrations.AddField(
            model_name='transmission',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='transmission'),
        ),
    ]
