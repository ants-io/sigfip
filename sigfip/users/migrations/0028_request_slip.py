# Generated by Django 2.2.6 on 2020-01-09 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20200109_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='slip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Slip', verbose_name='Bordereau'),
            preserve_default=False,
        ),
    ]
