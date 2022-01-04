# Generated by Django 4.0 on 2022-01-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('long_url', models.CharField(max_length=500)),
                ('short_url', models.CharField(max_length=500)),
            ],
        ),
    ]