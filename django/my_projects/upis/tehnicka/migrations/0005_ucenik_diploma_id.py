# Generated by Django 2.2.1 on 2019-05-19 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tehnicka', '0004_auto_20190519_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucenik',
            name='diploma_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tehnicka.Diploma'),
            preserve_default=False,
        ),
    ]