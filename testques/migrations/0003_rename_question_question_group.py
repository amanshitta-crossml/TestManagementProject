# Generated by Django 3.2.6 on 2021-08-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testques', '0002_auto_20210814_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='group',
        ),
    ]
