# Generated by Django 2.0.6 on 2019-03-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=200)),
                ('password', models.CharField(default=0, max_length=200)),
                ('date', models.DateField(default='')),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]