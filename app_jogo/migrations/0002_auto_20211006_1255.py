# Generated by Django 3.2.8 on 2021-10-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_jogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('sigla', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'produtora',
            },
        ),
        migrations.AddField(
            model_name='jogo',
            name='produtora',
            field=models.ManyToManyField(db_table='jogo_produtora', related_name='produtoras', to='app_jogo.Produtora'),
        ),
    ]
