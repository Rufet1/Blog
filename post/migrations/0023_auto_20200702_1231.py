# Generated by Django 3.0.8 on 2020-07-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_auto_20200702_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='bos'),
        ),
    ]
