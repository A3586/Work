# Generated by Django 3.1.2 on 2021-06-18 06:05

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210604_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='followers',
            new_name='favorites',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, help_text='Аватар', upload_to=main.models.profile_avatars, verbose_name='Ссылка картинки'),
        ),
    ]
