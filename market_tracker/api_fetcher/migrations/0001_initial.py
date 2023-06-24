# Generated by Django 4.1.7 on 2023-06-23 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockCom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Symbol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField()),
                ('Change_point', models.FloatField()),
                ('Change_percentage', models.FloatField()),
                ('Total_vol', models.FloatField()),
                ('Stock_symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_fetcher.stockcom')),
            ],
        ),
    ]
