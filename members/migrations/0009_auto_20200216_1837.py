# Generated by Django 3.0.3 on 2020-02-16 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20200216_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='full_name',
            new_name='display_name',
        ),
    ]
