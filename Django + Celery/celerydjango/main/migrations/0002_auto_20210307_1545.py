# Generated by Django 3.1.2 on 2021-03-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicon',
            name='dollar',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politicon',
            name='weather',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
