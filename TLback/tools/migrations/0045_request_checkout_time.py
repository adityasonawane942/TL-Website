# Generated by Django 3.0.7 on 2020-07-24 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0044_auto_20200724_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='checkout_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
