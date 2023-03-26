# Generated by Django 3.2.4 on 2022-01-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donation_plea_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=13)),
                ('organ', models.CharField(max_length=250)),
                ('birth_date', models.IntegerField()),
                ('birth_month', models.CharField(max_length=2)),
                ('birth_year', models.CharField(max_length=4)),
                ('message', models.TextField()),
            ],
        ),
    ]