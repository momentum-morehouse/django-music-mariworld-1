# Generated by Django 3.1.2 on 2020-10-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='img_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
