# Generated by Django 3.0.5 on 2020-05-09 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
