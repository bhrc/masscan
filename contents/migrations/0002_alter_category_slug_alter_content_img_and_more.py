# Generated by Django 4.0.6 on 2022-08-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='content',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='content',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
