# Generated by Django 4.1.3 on 2022-12-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_admindb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admindb',
            name='passs',
        ),
        migrations.AddField(
            model_name='admindb',
            name='pas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admindb',
            name='passwd',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
