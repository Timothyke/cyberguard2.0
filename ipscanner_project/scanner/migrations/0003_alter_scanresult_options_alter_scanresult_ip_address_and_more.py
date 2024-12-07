# Generated by Django 5.1.3 on 2024-12-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_scanresult_operating_system_scanresult_ports_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scanresult',
            options={'ordering': ['-scan_date'], 'verbose_name': 'Scan Result', 'verbose_name_plural': 'Scan Results'},
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='ip_address',
            field=models.GenericIPAddressField(db_index=True),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='scan_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='services',
            field=models.JSONField(default=dict),
        ),
    ]
