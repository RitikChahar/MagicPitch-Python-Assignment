# Generated by Django 5.0.4 on 2024-04-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_rename_user_id_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referred_by',
            field=models.CharField(max_length=100),
        ),
    ]