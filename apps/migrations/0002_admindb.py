# Generated by Django 4.1.3 on 2022-12-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mob', models.IntegerField(blank=True, max_length=100, null=True)),
                ('passs', models.IntegerField(blank=True, max_length=100, null=True)),
                ('passwd', models.IntegerField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
