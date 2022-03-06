# Generated by Django 4.0.2 on 2022-03-04 11:37
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sv_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServicesVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='services_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('title', models.CharField(max_length=250)),
                ('alt', models.TextField(null=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=11)),
                ('sv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name': 'Services Video',
                'verbose_name_plural': 'Services Videos',
            },
        ),
        migrations.CreateModel(
            name='ServicesPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('alt', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='services_images')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=11)),
                ('sv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name': 'Services Picture',
                'verbose_name_plural': 'Services Pictures',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pck_name', models.CharField(default='Package', max_length=250)),
                ('pck_price', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=11)),
                ('sv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
    ]
