# Generated by Django 5.0 on 2023-12-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_cooked_harmony', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
