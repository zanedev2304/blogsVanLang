# Generated by Django 4.1.7 on 2023-02-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApplicate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='default_author', max_length=200),
        ),
    ]
