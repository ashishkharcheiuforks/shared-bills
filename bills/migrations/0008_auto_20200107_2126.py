# Generated by Django 3.0.2 on 2020-01-07 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bills", "0007_auto_20200106_1928"),
    ]

    operations = [
        migrations.RemoveField(model_name="participant", name="user"),
        migrations.AddField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
