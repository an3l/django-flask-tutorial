# Generated by Django 2.2.1 on 2019-05-12 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_fligths_app', '0002_auto_20190512_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='_fligths_app.Flight')),
            ],
        ),
    ]