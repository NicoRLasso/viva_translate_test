# Generated by Django 4.0.9 on 2023-03-03 03:18

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('id_number', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('birthdate', models.DateField()),
                ('first_name', models.CharField(default='', max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
