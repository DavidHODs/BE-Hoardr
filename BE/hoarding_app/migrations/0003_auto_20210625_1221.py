# Generated by Django 3.1.7 on 2021-06-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoarding_app', '0002_auto_20210624_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
