# Generated by Django 3.1.7 on 2021-04-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0003_auto_20210417_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='other', max_length=50),
        ),
    ]
