# Generated by Django 5.0.2 on 2024-08-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='voto',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='candidato',
            name='foto',
            field=models.ImageField(default='candidatos/user.png', upload_to='candidatos/'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
