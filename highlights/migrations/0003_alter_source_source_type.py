# Generated by Django 4.2.7 on 2023-11-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("highlights", "0002_source_source_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="source",
            name="source_type",
            field=models.CharField(
                choices=[("book", "Book"), ("article", "Article"), ("other", "Other")],
                max_length=20,
                null=True,
            ),
        ),
    ]
