# Generated by Django 5.0.6 on 2024-05-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metaphysics', '0018_contactdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='location',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
