# Generated by Django 3.0.2 on 2020-01-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200128_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='vote_string',
            field=models.CharField(default='like', max_length=25),
        ),
    ]