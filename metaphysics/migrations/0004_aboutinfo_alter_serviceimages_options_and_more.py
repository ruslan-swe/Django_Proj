# Generated by Django 5.0.6 on 2024-05-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metaphysics', '0003_service_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(null=True, upload_to='about')),
                ('bottom_image', models.ImageField(null=True, upload_to='about')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('video_url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'About Info',
            },
        ),
        migrations.AlterModelOptions(
            name='serviceimages',
            options={'verbose_name_plural': 'Service Images'},
        ),
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
