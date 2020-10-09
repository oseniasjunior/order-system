# Generated by Django 3.1.2 on 2020-10-08 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeansPayment',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at')),
                ('active', models.BooleanField(db_column='active', default=True)),
                ('description', models.CharField(max_length=104, unique=True)),
            ],
            options={
                'db_table': 'means_payment',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at')),
                ('active', models.BooleanField(db_column='active', default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('O', 'Opened'), ('C', 'Closed'), ('X', 'Canceled'), ('P', 'Partial closed')], default='O', max_length=1)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at')),
                ('active', models.BooleanField(db_column='active', default=True)),
                ('name', models.CharField(max_length=104)),
                ('detail_description', models.TextField(null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at')),
                ('active', models.BooleanField(db_column='active', default=True)),
                ('number', models.IntegerField(unique=True)),
                ('status', models.CharField(choices=[('O', 'Occuped'), ('D', 'Desoccuped')], default='D', max_length=1)),
            ],
            options={
                'db_table': 'table',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='modified_at')),
                ('active', models.BooleanField(db_column='active', default=True)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(db_column='id_order', on_delete=django.db.models.deletion.DO_NOTHING, to='core.order')),
                ('product', models.ForeignKey(db_column='id_product', on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(db_column='id_table', on_delete=django.db.models.deletion.DO_NOTHING, to='core.table'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
