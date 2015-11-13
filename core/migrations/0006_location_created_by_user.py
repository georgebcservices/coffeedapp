# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20151111_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='created_by_user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
