# Generated by Django 2.2.6 on 2020-01-09 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20191212_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profession', verbose_name='Profession'),
        ),
        migrations.CreateModel(
            name='Slip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classed_date', models.DateField(verbose_name='Date de classification')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
