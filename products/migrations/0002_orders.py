# Generated by Django 5.1.4 on 2025-01-20 11:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.products')),
            ],
        ),
    ]
