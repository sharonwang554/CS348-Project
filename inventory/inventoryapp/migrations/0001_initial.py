# Generated by Django 3.2.9 on 2021-12-17 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_cost', models.IntegerField(default=0, verbose_name=models.DecimalField(decimal_places=2, max_digits=6))),
                ('item_price', models.IntegerField(default=0, verbose_name=models.DecimalField(decimal_places=2, max_digits=6))),
            ],
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10, null=True)),
                ('profit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1_q', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.customer')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.employee')),
                ('item1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_stock', models.IntegerField(default=0)),
                ('units_sold', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_profit_sold', models.IntegerField(default=0, verbose_name=models.DecimalField(decimal_places=2, max_digits=6))),
                ('number_items_sold', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(verbose_name=models.DecimalField(decimal_places=2, max_digits=6))),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_rewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewards_points', models.IntegerField(default=0)),
                ('has_rewards', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.customer')),
            ],
        ),
    ]
