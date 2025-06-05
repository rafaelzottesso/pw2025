from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Campus, Curso, TipoSolicitacao, Status, Aluno, Servidor, Solicitacao, Historico


class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'


class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'


class CampusCreate(CreateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Cadastrar Campus',
        'botao': 'Cadastrar',
    }
 

class CursoCreate(CreateView):
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Cadastrar Curso',
        'botao': 'Cadastrar',
    }


class TipoSolicitacaoCreate(CreateView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Tipo de Solicitação',
        'botao': 'Cadastrar',
    }


class StatusCreate(CreateView):
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Status',
        'botao': 'Cadastrar',
    }


class AlunoCreate(CreateView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matrícula', 'cpf', 'email', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Aluno',
        'botao': 'Cadastrar',
    }


class ServidorCreate(CreateView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'siape', 'email']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Servidor',
        'botao': 'Cadastrar',
    }


class SolicitacaoCreate(CreateView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    fields = ['solicitado_por', 'curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Protocolo online da Secretaria',
        'botao': 'Protocolar',
    }


class HistoricoCreate(CreateView):
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Histórico',
        'botao': 'Cadastrar',
    }


##################################################


class CampusUpdate(UpdateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Atualização de dados do Campus',
        'botao': 'Salvar',
    }


class CursoUpdate(UpdateView):
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Atualização de dados do Curso',
        'botao': 'Salvar',
    }


class TipoSolicitacaoUpdate(UpdateView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Tipo de Solicitação',
        'botao': 'Salvar',
    }


class StatusUpdate(UpdateView):
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Status',
        'botao': 'Salvar',
    }


class AlunoUpdate(UpdateView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matrícula', 'cpf', 'email', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Aluno',
        'botao': 'Salvar',
    }


class ServidorUpdate(UpdateView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'siape', 'email']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Servidor',
        'botao': 'Salvar',
    }


class SolicitacaoUpdate(UpdateView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    fields = ['solicitado_por', 'curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados da Solicitação',
        'botao': 'Salvar',
    }


class HistoricoUpdate(UpdateView):
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Histórico',
        'botao': 'Salvar',
    }


##################################################


class CampusDelete(DeleteView):
    model = Campus
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Excluir Campus',
        'botao': 'Excluir',
    }


class CursoDelete(DeleteView):
    model = Curso
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Excluir Curso',
        'botao': 'Excluir',
    }


class TipoSolicitacaoDelete(DeleteView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Tipo de Solicitação',
        'botao': 'Excluir',
    }


class StatusDelete(DeleteView):
    model = Status
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Status',
        'botao': 'Excluir',
    }


class AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Aluno',
        'botao': 'Excluir',
    }


class ServidorDelete(DeleteView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Servidor',
        'botao': 'Excluir',
    }


class SolicitacaoDelete(DeleteView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Solicitação',
        'botao': 'Excluir',
    }


class HistoricoDelete(DeleteView):
    model = Historico
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Histórico',
        'botao': 'Excluir',
    }


##################################################


class CampusList(ListView):
    model = Campus
    template_name = 'paginasweb/listas/campus.html'
    

class CursoList(ListView):
    model = Curso
    template_name = 'paginasweb/listas/curso.html'


class TipoSolicitacaoList(ListView):
    model = TipoSolicitacao
    template_name = 'paginasweb/listas/tipo_solicitacao.html'


class StatusList(ListView):
    model = Status
    template_name = 'paginasweb/listas/status.html'


class AlunoList(ListView):
    model = Aluno
    template_name = 'paginasweb/listas/aluno.html'


class ServidorList(ListView):
    model = Servidor
    template_name = 'paginasweb/listas/servidor.html'


class SolicitacaoList(ListView):
    model = Solicitacao
    template_name = 'paginasweb/listas/solicitacao.html'


class HistoricoList(ListView):
    model = Historico
    template_name = 'paginasweb/listas/historico.html'
