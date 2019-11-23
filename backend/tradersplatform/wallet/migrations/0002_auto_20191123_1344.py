# Generated by Django 2.2.6 on 2019-11-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='AAPL',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='BTC',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='ETH',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='EUR',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='GBP',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='GM',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='GOOGL',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='IVV',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='LTC',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='SPY',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='Sent_USD',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='TRY',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='USD',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='VTI',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='Wealth_USD',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='XAG',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='XAU',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='XRH',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=20, null=True),
        ),
    ]
