# Generated by Django 3.0.2 on 2020-01-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200130_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='voted_product',
            name='string',
            field=models.CharField(default='like', max_length=20),
        ),
    ]
