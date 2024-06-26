# Generated by Django 5.0.4 on 2024-04-07 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_user', models.CharField(max_length=100)),
                ('referral_points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.user')),
            ],
        ),
    ]
