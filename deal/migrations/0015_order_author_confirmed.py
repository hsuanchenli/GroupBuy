# Generated by Django 2.1.4 on 2018-12-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0014_auto_20181219_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='author_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
