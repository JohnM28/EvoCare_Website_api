
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=40)),
                ('is_verified', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40, null=True)),
                ('feedback', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time', models.CharField(max_length=30, unique=True)),
                ('Last_Name', models.CharField(max_length=30)),
                ('First_Name', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('User_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]
