# Generated by Django 3.0.2 on 2020-01-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200128_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='full_name',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]