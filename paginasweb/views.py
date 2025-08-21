from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Campus, Curso, TipoSolicitacao, Status, Aluno, Servidor, Solicitacao, Historico

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Usuário',
        'botao': 'Cadastrar',
    }

    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Estudante')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        # Retorna a URL de sucesso
        return url

class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'


class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'


class CampusCreate(LoginRequiredMixin, CreateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Cadastrar Campus',
        'botao': 'Cadastrar',
    }
 

class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Cadastrar Curso',
        'botao': 'Cadastrar',
    }


class TipoSolicitacaoCreate(LoginRequiredMixin, CreateView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Cadastrar Tipo de Solicitação',
        'botao': 'Cadastrar',
    }


class StatusCreate(LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('listar-status')
    extra_context = {
        'titulo': 'Cadastrar Status',
        'botao': 'Cadastrar',
    }


class AlunoCreate(LoginRequiredMixin, CreateView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matricula', 'cpf', 'telefone']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {
        'titulo': 'Cadastrar Aluno',
        'botao': 'Cadastrar',
    }


class ServidorCreate(LoginRequiredMixin, CreateView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'siape']
    success_url = reverse_lazy('listar-servidor')
    extra_context = {
        'titulo': 'Cadastrar Servidor',
        'botao': 'Cadastrar',
    }


class SolicitacaoCreate(LoginRequiredMixin, CreateView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    # Remove do fields o atributo que tem relação com User - solicitado_por
    fields = ['curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('listar-solicitacao')
    extra_context = {
        'titulo': 'Protocolo online da Secretaria',
        'botao': 'Protocolar', 
    }

    def form_valid(self, form):
        # pegar o usuário que está autenticado
        form.instance.solicitado_por = self.request.user
        url = super().form_valid(form)
        return url



class HistoricoCreate(LoginRequiredMixin, CreateView):
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('listar-historico')
    extra_context = {
        'titulo': 'Cadastrar Histórico',
        'botao': 'Cadastrar',
    }


##################################################


class CampusUpdate(LoginRequiredMixin, UpdateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Atualização de dados do Campus',
        'botao': 'Salvar',
    }


class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Atualização de dados do Curso',
        'botao': 'Salvar',
    }


class TipoSolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Atualização de dados do Tipo de Solicitação',
        'botao': 'Salvar',
    }


class StatusUpdate(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('listar-status')
    extra_context = {
        'titulo': 'Atualização de dados do Status',
        'botao': 'Salvar',
    }


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matricula', 'cpf', 'telefone']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {
        'titulo': 'Atualização de dados do Aluno',
        'botao': 'Salvar',
    }


class ServidorUpdate(LoginRequiredMixin, UpdateView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'siape']
    success_url = reverse_lazy('listar-servidor')
    extra_context = {
        'titulo': 'Atualização de dados do Servidor',
        'botao': 'Salvar',
    }


class SolicitacaoUpdate(LoginRequiredMixin, UpdateView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    fields = ['solicitado_por', 'curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('listar-solicitacao')
    extra_context = {
        'titulo': 'Atualização de dados da Solicitação',
        'botao': 'Salvar',
    }


class HistoricoUpdate(LoginRequiredMixin, UpdateView):
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('listar-historico')
    extra_context = {
        'titulo': 'Atualização de dados do Histórico',
        'botao': 'Salvar',
    }


##################################################


class CampusDelete(LoginRequiredMixin, DeleteView):
    model = Campus
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Excluir Campus',
        'botao': 'Excluir',
    }


class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Excluir Curso',
        'botao': 'Excluir',
    }


class TipoSolicitacaoDelete(LoginRequiredMixin, DeleteView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Excluir Tipo de Solicitação',
        'botao': 'Excluir',
    }


class StatusDelete(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-status')
    extra_context = {
        'titulo': 'Excluir Status',
        'botao': 'Excluir',
    }


class AlunoDelete(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-aluno')
    extra_context = {
        'titulo': 'Excluir Aluno',
        'botao': 'Excluir',
    }


class ServidorDelete(LoginRequiredMixin, DeleteView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-servidor')
    extra_context = {
        'titulo': 'Excluir Servidor',
        'botao': 'Excluir',
    }


class SolicitacaoDelete(LoginRequiredMixin, DeleteView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-solicitacao')
    extra_context = {
        'titulo': 'Excluir Solicitação',
        'botao': 'Excluir',
    }


class HistoricoDelete(LoginRequiredMixin, DeleteView):
    model = Historico
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-historico')
    extra_context = {
        'titulo': 'Excluir Histórico',
        'botao': 'Excluir',
    }


##################################################


class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = 'paginasweb/listas/campus.html'
    

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'paginasweb/listas/curso.html'


class TipoSolicitacaoList(LoginRequiredMixin, ListView):
    model = TipoSolicitacao
    template_name = 'paginasweb/listas/tipo-solicitacao.html'


class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'paginasweb/listas/status.html'


class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'paginasweb/listas/aluno.html'


class ServidorList(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = 'paginasweb/listas/servidor.html'


class SolicitacaoList(LoginRequiredMixin, ListView):
    model = Solicitacao
    template_name = 'paginasweb/listas/solicitacao.html'


class HistoricoList(LoginRequiredMixin, ListView):
    model = Historico
    template_name = 'paginasweb/listas/historico.html'
