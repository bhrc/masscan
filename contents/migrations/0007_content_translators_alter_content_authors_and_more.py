# Generated by Django 4.0.6 on 2022-08-17 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_geotag_amar_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='translators',
            field=models.ManyToManyField(blank=True, related_name='translators', to='contents.author'),
        ),
        migrations.AlterField(
            model_name='content',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='authors', to='contents.author'),
        ),
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(blank=True, to='contents.category'),
        ),
        migrations.AlterField(
            model_name='content',
            name='geotags',
            field=models.ManyToManyField(blank=True, to='contents.geotag'),
        ),
        migrations.AlterField(
            model_name='content',
            name='publication',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contents.publication'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, to='contents.tag'),
        ),
    ]