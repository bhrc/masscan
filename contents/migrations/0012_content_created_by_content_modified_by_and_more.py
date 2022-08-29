# Generated by Django 4.0.6 on 2022-08-28 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_alter_content_pub_date_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created_by',
            field=models.CharField(blank=True, default='maskan', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='modified_by',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
