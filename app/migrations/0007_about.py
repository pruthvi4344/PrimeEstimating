# Generated by Django 5.1.4 on 2025-01-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.CharField(max_length=1000)),
                ('experience', models.IntegerField()),
                ('procom', models.IntegerField()),
                ('satisfaction', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=300)),
                ('icon_class', models.CharField(default='fas fa-cogs', max_length=100)),
            ],
        ),
    ]
