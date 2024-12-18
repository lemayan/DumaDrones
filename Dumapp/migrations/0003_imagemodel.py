# Generated by Django 5.1.4 on 2024-12-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('delivery_address', models.TextField(max_length=300)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]
