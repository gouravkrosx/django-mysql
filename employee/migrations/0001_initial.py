# Generated by Django 4.2.7 on 2025-07-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years_of_experience', models.IntegerField()),
                ('field_of_expertise', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
