# Generated by Django 4.0.1 on 2022-03-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
