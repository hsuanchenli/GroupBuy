# Generated by Django 2.1.4 on 2018-12-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='target_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
