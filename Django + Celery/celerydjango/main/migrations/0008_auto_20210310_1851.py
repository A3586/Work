# Generated by Django 3.1.2 on 2021-03-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210310_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(),
        ),
    ]
