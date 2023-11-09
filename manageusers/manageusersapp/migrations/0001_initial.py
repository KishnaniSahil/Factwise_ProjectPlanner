# Generated by Django 4.2.7 on 2023-11-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('display_name', models.CharField(max_length=64)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
