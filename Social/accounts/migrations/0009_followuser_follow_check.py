# Generated by Django 3.0.5 on 2020-06-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200629_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='followuser',
            name='follow_check',
            field=models.BooleanField(default=True),
        ),
    ]
