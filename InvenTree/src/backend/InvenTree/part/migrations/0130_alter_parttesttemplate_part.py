# Generated by Django 4.2.15 on 2024-08-29 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0129_auto_20240815_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parttesttemplate',
            name='part',
            field=models.ForeignKey(limit_choices_to={'testable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='test_templates', to='part.part', verbose_name='Part'),
        ),
    ]
