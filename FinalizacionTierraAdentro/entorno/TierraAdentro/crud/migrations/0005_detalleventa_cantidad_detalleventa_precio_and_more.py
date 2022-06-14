# Generated by Django 4.0.1 on 2022-06-07 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_detalleventa_venta_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='precio',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(blank=True, db_column='producto_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(blank=True, db_column='venta_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='crud.venta'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crud.cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.TextField(default='En espera', max_length=30),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='fecha creacion'),
        ),
        migrations.AddField(
            model_name='venta',
            name='hora',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
