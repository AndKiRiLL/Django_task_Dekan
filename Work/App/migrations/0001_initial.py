# Generated by Django 5.0 on 2023-12-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Page1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('price', models.CharField(max_length=35)),
                ('path_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_Page2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('price', models.CharField(max_length=35)),
                ('path_img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_Page3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('price', models.CharField(max_length=35)),
                ('path_img', models.TextField()),
            ],
        ),
    ]
