# Generated by Django 3.0.5 on 2020-04-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hit",
            name="tracker",
            field=models.TextField(
                choices=[("JS", "JavaScript"), ("PIXEL", "Pixel (noscript)")]
            ),
        ),
    ]
