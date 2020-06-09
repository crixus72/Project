# Generated by Django 3.0.6 on 2020-06-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=400)),
                ('timestamp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_id', models.CharField(max_length=255)),
            ],
        ),
    ]