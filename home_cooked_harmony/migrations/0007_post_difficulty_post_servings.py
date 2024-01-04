# Generated by Django 5.0 on 2024-01-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_cooked_harmony', '0006_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='difficulty',
            field=models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='E', max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='servings',
            field=models.CharField(choices=[('1', '1'), ('1-2', '1-2'), ('2-4', '2-4'), ('4+', '4+')], default='1', max_length=3),
        ),
    ]