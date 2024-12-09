# Generated by Django 5.1.3 on 2024-12-09 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_alter_scanresult_options_alter_scanresult_ip_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=255)),
                ('details', models.TextField(blank=True, null=True)),
                ('scan_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='scanner.scanresult')),
            ],
            options={
                'verbose_name': 'Scan Activity',
                'verbose_name_plural': 'Scan Activities',
                'ordering': ['-timestamp'],
            },
        ),
    ]