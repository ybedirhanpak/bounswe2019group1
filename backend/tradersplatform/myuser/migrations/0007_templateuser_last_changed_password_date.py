# Generated by Django 2.2.6 on 2019-10-09 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0006_auto_20191002_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateuser',
            name='last_changed_password_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]