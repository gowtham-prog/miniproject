# Generated by Django 3.2.9 on 2021-12-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20211228_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.URLField(blank=True),
        ),
    ]
