# Generated by Django 4.0.6 on 2022-08-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0003_alter_shorturl_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='complete_url',
            field=models.URLField(db_index=True, unique=True),
        ),
    ]
