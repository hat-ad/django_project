# Generated by Django 3.0.5 on 2020-06-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='follo_wers',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.follow'),
            preserve_default=False,
        ),
    ]