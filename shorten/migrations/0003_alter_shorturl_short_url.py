# Generated by Django 4.0.6 on 2022-08-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_alter_shorturl_complete_url_alter_shorturl_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.URLField(),
        ),
    ]
