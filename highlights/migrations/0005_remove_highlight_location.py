# Generated by Django 4.2.7 on 2023-11-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("highlights", "0004_alter_source_source_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="highlight",
            name="location",
        ),
    ]
