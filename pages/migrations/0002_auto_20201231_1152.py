# Generated by Django 3.1.2 on 2020-12-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial',
            name='phone_cable_internet_expenses',
        ),
        migrations.AddField(
            model_name='financial',
            name='telecom_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='alert_type',
            field=models.CharField(choices=[('Saldo bajo en cuenta', 'Saldo bajo en cuenta'), ('Movimientos duplicados', 'Movimientos duplicados'), ('Resumen semanal de tu control financiero', 'Resumen semanal de tu control financiero'), ('Resumen mensual de tu control financiero', 'Resumen mensual de tu control financiero'), ('Proyección del ahorro', 'Proyección del ahorro'), ('Dinero restante por cumplir la cuota mensual de ahorro', 'Dinero restante por cumplir la cuota mensual de ahorro')], max_length=100),
        ),
        migrations.AlterField(
            model_name='financial',
            name='billing_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='clothing_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='common_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='education_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='emergency_fund',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='entertainment_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='extra_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='fixed_income2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='fixed_income3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='food_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='health_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='insurance_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='media',
            field=models.CharField(choices=[('Whatsapp', 'Whatsapp'), ('Email', 'Email')], max_length=20),
        ),
        migrations.AlterField(
            model_name='financial',
            name='objective',
            field=models.CharField(choices=[('Comprar un departamento o casa', 'Comprar un departamento o casa'), ('Pagar mi educación', 'Pagar mi educación'), ('Viajar', 'Viajar'), ('Emprender un negocio o nuevo proyecto', 'Emprender un negocio o nuevo proyecto'), ('Para mi jubilación', 'Para mi jubilación'), ('Invertir mi dinero', 'Invertir mi dinero'), ('Pagar algún tipo de seguro o deuda', 'Pagar algún tipo de seguro o deuda'), ('Otro objetivo de ahorro', 'Otro objetivo de ahorro'), ('No tengo ningún objetivo de ahorro en mente', 'No tengo ningún objetivo de ahorro en mente')], max_length=100),
        ),
        migrations.AlterField(
            model_name='financial',
            name='rent_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='subscription_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='transport_expenses',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]