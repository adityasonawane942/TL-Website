# Generated by Django 3.0.5 on 2020-06-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0031_merge_20200617_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
