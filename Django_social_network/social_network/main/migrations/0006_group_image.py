# Generated by Django 3.1.2 on 2021-04-08 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210330_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, help_text='Аватар группы', upload_to='images/group/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
    ]
