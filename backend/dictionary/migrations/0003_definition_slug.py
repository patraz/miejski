# Generated by Django 4.2.1 on 2023-05-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dictionary", "0002_definition_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="definition",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
