# Generated by Django 5.1 on 2024-09-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
