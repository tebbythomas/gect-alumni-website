# Generated by Django 3.0.3 on 2020-02-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20200217_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, default='default/default-profile.jpg', upload_to='member/%Y/%m/%d/'),
        ),
    ]
