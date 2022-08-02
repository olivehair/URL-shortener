# Generated by Django 4.0.6 on 2022-08-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='complete_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.URLField(max_length=300),
        ),
    ]