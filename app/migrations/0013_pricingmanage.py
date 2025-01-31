# Generated by Django 5.1.4 on 2025-01-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricingmanage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('line', models.CharField(max_length=100)),
                ('button_text', models.CharField(max_length=10)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='servicewelcome/')),
            ],
        ),
    ]
