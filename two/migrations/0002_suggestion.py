# Generated by Django 4.2.6 on 2023-11-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('text', models.CharField(max_length=300)),
            ],
        ),
    ]
