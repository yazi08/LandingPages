# Generated by Django 3.1.7 on 2021-04-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chai',
            name='photo',
            field=models.ImageField(null=True, upload_to='чай'),
        ),
    ]
