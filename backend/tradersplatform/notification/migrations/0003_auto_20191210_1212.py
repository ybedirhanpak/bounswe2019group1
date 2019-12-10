# Generated by Django 2.2.6 on 2019-12-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0007_auto_20191124_1437'),
        ('notification', '0002_auto_20191209_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='SetNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='owner_notif', to='myuser.TemplateUser')),
            ],
        ),
    ]
