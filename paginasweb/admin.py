from django.contrib import admin
from .models import Aluno, Campus, Curso, Historico, Servidor, Solicitacao, Status, TipoSolicitacao

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Campus)
admin.site.register(Curso)
admin.site.register(Historico)
admin.site.register(Servidor)
admin.site.register(Solicitacao)
admin.site.register(Status)
admin.site.register(TipoSolicitacao)