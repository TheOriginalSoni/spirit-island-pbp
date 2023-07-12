# Generated by Django 4.0.1 on 2023-07-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0026_auto_20230707_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameplayer',
            name='healing',
            field=models.ManyToManyField(blank=True, related_name='healing', to='pbf.Card'),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.IntegerField(choices=[(0, 'Minor'), (1, 'Major'), (2, 'Unique'), (3, 'Special')]),
        ),
    ]