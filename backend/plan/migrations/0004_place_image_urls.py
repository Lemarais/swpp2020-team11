# Generated by Django 3.1.2 on 2020-11-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_review_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image_urls',
            field=models.URLField(null=True),
        ),
    ]
