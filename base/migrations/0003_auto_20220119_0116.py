# Generated by Django 3.1.4 on 2022-01-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220118_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='_id',
        ),
    ]
