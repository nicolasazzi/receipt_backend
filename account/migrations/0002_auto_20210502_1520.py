# Generated by Django 3.1.7 on 2021-05-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
