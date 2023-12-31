# Generated by Django 4.2.1 on 2023-07-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('last_online', models.DateTimeField(auto_now=True)),
                ('host', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('os', models.CharField(max_length=50)),
                ('os_version', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commands', models.ManyToManyField(blank=True, to='C2.command')),
            ],
        ),
    ]
