# Generated by Django 4.2.1 on 2023-05-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Bullseye Blog', max_length=255),
        ),
    ]
