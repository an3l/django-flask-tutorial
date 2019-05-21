# Generated by Django 2.2.1 on 2019-05-14 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(default='MM', max_length=2)),
                ('naziv', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Predmet',
                'verbose_name_plural': 'Predmeti',
            },
        ),
        migrations.CreateModel(
            name='Smjer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(default='AUT', max_length=3)),
                ('naziv', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'smjerovi',
            },
        ),
        migrations.CreateModel(
            name='Ucenik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('JMBG', models.IntegerField(blank=True, null=True)),
                ('smjer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tehnicka.Smjer')),
            ],
            options={
                'verbose_name_plural': 'Učenici',
            },
        ),
        migrations.CreateModel(
            name='Ocjena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocjena', models.IntegerField()),
                ('predmet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tehnicka.Predmet')),
                ('ucenik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tehnicka.Ucenik')),
            ],
            options={
                'verbose_name': 'Ocjena',
                'verbose_name_plural': 'Ocjene',
            },
        ),
    ]