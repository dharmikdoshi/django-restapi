# Generated by Django 2.2 on 2021-11-07 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'advisors',
            },
        ),
        migrations.CreateModel(
            name='BookingAdvisorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.CharField(max_length=255)),
                ('advisor_id', models.ForeignKey(db_column='advisor_id', on_delete=django.db.models.deletion.PROTECT, related_name='booking', to='first.AdvisorModel')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
