# Generated by Django 2.2.6 on 2019-11-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EUR', models.CharField(blank=True, max_length=300, null=True)),
                ('GBP', models.CharField(max_length=300)),
                ('TRY', models.CharField(max_length=300)),
            ],
        ),
    ]