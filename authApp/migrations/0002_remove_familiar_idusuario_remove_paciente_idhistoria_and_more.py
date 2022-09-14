# Generated by Django 4.1.1 on 2022-09-14 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='idusuario',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='idhistoria',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='idpaciente',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='idpersonal_salud',
        ),
        migrations.AddField(
            model_name='historia',
            name='idpaciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='historia', to='authApp.paciente'),
        ),
        migrations.AddField(
            model_name='personalsalud',
            name='idusuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='personalSalud', to='authApp.usuario'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='idpaciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='authApp.paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idpersonal_salud',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.personalsalud'),
        ),
        migrations.AlterField(
            model_name='signos',
            name='idpaciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='signos', to='authApp.paciente'),
        ),
    ]
