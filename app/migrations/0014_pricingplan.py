# Generated by Django 5.1.4 on 2025-02-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_pricingmanage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(help_text="Use 'Custom' for variable pricing", max_length=50)),
                ('features', models.TextField(help_text='Enter features separated by commas')),
                ('button_text', models.CharField(default='Get Started', max_length=50)),
                ('button_link', models.URLField(default='#')),
                ('most_popular', models.BooleanField(default=False)),
            ],
        ),
    ]
