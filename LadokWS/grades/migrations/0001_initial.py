# Generated by Django 2.1 on 2018-11-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideal', models.CharField(max_length=10)),
                ('enroll_code', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=3)),
            ],
        ),
    ]