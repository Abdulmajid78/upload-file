# Generated by Django 4.2.10 on 2024-02-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='file',
            field=models.FileField(default=None, upload_to='files/'),
            preserve_default=False,
        ),
    ]