# Generated by Django 2.2 on 2019-05-20 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('part', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierpart',
            name='part',
            field=models.ForeignKey(help_text='Select part', limit_choices_to={'purchaseable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_parts', to='part.Part'),
        ),
        migrations.AddField(
            model_name='supplierpart',
            name='supplier',
            field=models.ForeignKey(help_text='Select supplier', limit_choices_to={'is_supplier': True}, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='company.Company'),
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='company.Company'),
        ),
        migrations.AlterUniqueTogether(
            name='supplierpricebreak',
            unique_together={('part', 'quantity')},
        ),
        migrations.AlterUniqueTogether(
            name='supplierpart',
            unique_together={('part', 'supplier', 'SKU')},
        ),
    ]
