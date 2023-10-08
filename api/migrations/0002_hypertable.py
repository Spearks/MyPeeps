from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT create_hypertable('api_peepsmetric', 'time', chunk_time_interval => INTERVAL '1 day')"
        )
    ]