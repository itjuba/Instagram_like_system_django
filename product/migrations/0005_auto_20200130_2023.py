# Generated by Django 3.0.2 on 2020-01-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_voted_product_vote_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voted_product',
            name='vote_number',
            field=models.CharField(default='voted', max_length=100),
        ),
    ]
