# Generated by Django 2.2.6 on 2019-10-31 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='corps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Corps', verbose_name='Corps'),
            preserve_default=False,
        ),
    ]
