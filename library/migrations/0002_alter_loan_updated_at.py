# Generated by Django 5.1 on 2024-10-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
