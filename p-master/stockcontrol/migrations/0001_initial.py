# Generated by Django 5.0.2 on 2024-02-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('supplier', models.CharField(blank=True, max_length=255)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]