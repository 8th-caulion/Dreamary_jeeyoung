# Generated by Django 3.0.9 on 2020-08-04 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designer',
            old_name='desciption',
            new_name='description',
        ),
    ]
