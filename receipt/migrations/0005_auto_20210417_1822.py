# Generated by Django 3.1.7 on 2021-04-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0004_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(default='pcs', max_length=10),
        ),
    ]
