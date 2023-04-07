# Generated by Django 4.1.6 on 2023-04-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0007_remove_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='', upload_to='static')),
            ],
        ),
    ]