# Generated by Django 4.0.2 on 2022-02-18 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_services_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='pck_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='packages',
            name='sv_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services'),
        ),
    ]
