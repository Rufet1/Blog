# Generated by Django 2.2.6 on 2020-02-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_postlike'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]
