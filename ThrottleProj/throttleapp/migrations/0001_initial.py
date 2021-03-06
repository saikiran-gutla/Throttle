# Generated by Django 3.1 on 2020-08-16 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('User_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='ActivityPeriodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Activity', to='throttleapp.usermodel')),
            ],
            options={
                'verbose_name_plural': 'ActivityPeriods',
            },
        ),
    ]
