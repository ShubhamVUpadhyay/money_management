# Generated by Django 3.2.7 on 2024-01-10 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income_details', '0002_rename_user_income_user_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='user',
            new_name='user_info',
        ),
    ]
