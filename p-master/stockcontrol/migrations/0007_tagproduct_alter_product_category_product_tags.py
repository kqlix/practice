# Generated by Django 5.0.2 on 2024-02-28 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockcontrol', '0006_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='stockcontrol.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='stockcontrol.tagproduct'),
        ),
    ]
