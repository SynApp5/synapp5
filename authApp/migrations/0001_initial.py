# Generated by Django 4.1.1 on 2022-09-17 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('genero', models.CharField(max_length=45, verbose_name='Género')),
                ('perfil', models.CharField(max_length=45, verbose_name='Perfil')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idpaciente', models.AutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=45, verbose_name='Ciudad')),
                ('fecha_nac', models.CharField(max_length=45, verbose_name='Fecha nacimiento')),
                ('direccion', models.CharField(max_length=10, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Signos',
            fields=[
                ('idsignos', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.IntegerField(default=0, verbose_name='Oximetria')),
                ('frec_cardiaca', models.IntegerField(default=0, verbose_name='Frecuencia Cardiaca')),
                ('frec_respiratoria', models.IntegerField(default=0, verbose_name='Frecuencia Respiratoria')),
                ('temperatura', models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='Temperatura')),
                ('presion_arterial', models.IntegerField(default=0, verbose_name='Presión Arterial')),
                ('glicemias', models.CharField(max_length=45, verbose_name='Glicemias')),
                ('fecha', models.DateTimeField(max_length=45, verbose_name='Fecha')),
                ('idpaciente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='signos', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='personalSalud',
            fields=[
                ('idpersonal_salud', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=45, verbose_name='Especialidad')),
                ('registro', models.CharField(max_length=45, verbose_name='Registro Médico')),
                ('rol', models.CharField(max_length=45, verbose_name='Rol')),
                ('idusuario', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='personal_salud', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='idpersonal_salud',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.personalsalud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('idhistoria', models.AutoField(primary_key=True, serialize=False)),
                ('sugerencia', models.CharField(max_length=45, verbose_name='Sugerencia')),
                ('diagnostico', models.CharField(max_length=45, verbose_name='Diagnostico')),
                ('entorno', models.CharField(max_length=45, verbose_name='Entorno')),
                ('fecha', models.DateField(max_length=45, verbose_name='Fecha')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripcion')),
                ('idpaciente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='historia', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('idfamiliar', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=45, verbose_name='Parentesco')),
                ('correo', models.CharField(max_length=45, verbose_name='Correo')),
                ('idpaciente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='authApp.paciente')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
