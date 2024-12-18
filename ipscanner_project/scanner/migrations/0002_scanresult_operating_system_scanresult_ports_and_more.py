# Generated by Django 5.1.3 on 2024-12-06 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='operating_system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='ports',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='scan_duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='scan_type',
            field=models.CharField(choices=[('fast', 'Fast Scan'), ('full', 'Full Scan')], default='fast', max_length=20),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='services',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='status',
            field=models.CharField(choices=[('success', 'Success'), ('failed', 'Failed')], default='success', max_length=50),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
