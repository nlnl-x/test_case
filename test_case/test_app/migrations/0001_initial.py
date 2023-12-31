# Generated by Django 4.2.6 on 2023-10-05 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=3, max_digits=15)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.currency')),
            ],
            options={
                'unique_together': {('currency', 'date')},
            },
        ),
    ]
