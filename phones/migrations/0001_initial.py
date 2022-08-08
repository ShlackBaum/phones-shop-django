# Generated by Django 4.1 on 2022-08-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=300)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(max_length=50)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
