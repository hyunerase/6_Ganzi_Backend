# Generated by Django 5.1.3 on 2024-11-19 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_kakao_access_token'),
        ('sch_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='badge_condition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='badge',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sch_requests.category'),
        ),
    ]