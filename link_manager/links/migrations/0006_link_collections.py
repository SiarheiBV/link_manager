# Generated by Django 5.0.4 on 2024-04-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0005_collection_created_at_collection_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="collections",
            field=models.ManyToManyField(related_name="links", to="links.collection"),
        ),
    ]
