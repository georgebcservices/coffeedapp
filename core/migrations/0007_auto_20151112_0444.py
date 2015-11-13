# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_location_created_by_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='created_by_user',
            new_name='user',
        ),
    ]
