# Generated by Django 3.1.7 on 2021-04-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0002_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]