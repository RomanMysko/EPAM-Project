# Generated by Django 3.1.3 on 2021-05-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20210504_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.TextField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
