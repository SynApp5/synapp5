from django.contrib import admin
from .models.familiar import Familiar
from .models.personal_salud import personalSalud
from .models.paciente import Paciente
from .models.signos import Signos
from .models.usuario import Usuario
from .models.historia import Historia

admin.site.register(Familiar)
admin.site.register(personalSalud)
admin.site.register(Paciente)
admin.site.register(Signos)
admin.site.register(Usuario)
admin.site.register(Historia)