# Generated by Django 4.0.4 on 2023-06-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0011_remove_usuario_id_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('A', 'Avancado'), ('B', 'Intermediário'), ('C', 'Básico')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='data',
            field=models.DateField(default='0001-01-01', max_length=10, null=True),
        ),
    ]
