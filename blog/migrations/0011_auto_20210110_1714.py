# Generated by Django 3.1.5 on 2021-01-10 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210110_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='instagram_uel',
            new_name='instagram_url',
        ),
    ]