# Generated by Django 4.0.2 on 2022-03-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user_id',
        ),
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('Show', 'Show'), ('Hide', 'Hide')], default='Hide', max_length=11),
        ),
    ]