# Generated by Django 3.1.2 on 2021-05-22 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_document_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('above_folder', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.folder')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.repository')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='folder',
            field=models.ForeignKey(blank=True, default=4, on_delete=django.db.models.deletion.CASCADE, to='main.folder'),
            preserve_default=False,
        ),
    ]