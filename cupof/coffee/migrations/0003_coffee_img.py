# Generated by Django 3.1.7 on 2021-04-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20210404_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='img',
            field=models.ImageField(null=True, upload_to='coffee'),
        ),
    ]