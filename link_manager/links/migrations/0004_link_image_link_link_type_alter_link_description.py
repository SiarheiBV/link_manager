# Generated by Django 5.0.4 on 2024-04-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0003_link_created_at_link_description_link_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="link",
            name="link_type",
            field=models.CharField(
                choices=[
                    ("website", "Website"),
                    ("book", "Book"),
                    ("article", "Article"),
                    ("music", "Music"),
                    ("video", "Video"),
                ],
                default="website",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="link",
            name="description",
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
