# Generated by Django 5.0.6 on 2024-11-22 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productcomment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='status',
            field=models.CharField(choices=[('C', 'Checked'), ('NC', 'Not-Checked')], default='NC', max_length=255),
        ),
    ]
