# Generated by Django 3.2.7 on 2021-09-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=9)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('married', models.BooleanField()),
            ],
        ),
    ]
