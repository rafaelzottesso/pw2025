from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Campus, Curso, TipoSolicitacao, Status, Aluno, Servidor, Solicitacao, Historico

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm, AlunoCadastroForm, ServidorCadastroForm


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


class CadastroAlunoView(CreateView):
    model = User
    form_class = AlunoCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Aluno',
        'botao': 'Cadastrar',
    }

    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Estudantes')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        
        # Criar o registro de Aluno associado ao usuário
        Aluno.objects.create(
            nome=form.cleaned_data['nome'],
            matricula=form.cleaned_data['matricula'],
            cpf=form.cleaned_data['cpf'],
            telefone=form.cleaned_data['telefone'],
            usuario=self.object
        )
        
        # Retorna a URL de sucesso
        return url


class CadastroServidorView(CreateView):
    model = User
    form_class = ServidorCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Servidor',
        'botao': 'Cadastrar',
    }

    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Servidores')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        
        # Criar o registro de Servidor associado ao usuário
        Servidor.objects.create(
            nome=form.cleaned_data['nome'],
            siape=form.cleaned_data['siape'],
            usuario=self.object
        )
        
        # Retorna a URL de sucesso
        return url

class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qtde_campus"] = Campus.objects.all().count()
        context["qtde_cursos"] = Curso.objects.all().count()
        context["qtde_solicitacoes"] = Solicitacao.objects.all().count()
        context["tiposSolicitacoes"] = TipoSolicitacao.objects.all()
        return context


class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'


class CampusCreate(GroupRequiredMixin, CreateView):
    group_required = [ "Administrador", "Gerente", "Supervisor" ]
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Cadastrar Campus',
        'botao': 'Cadastrar',
    }
 

class CursoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Cadastrar Curso',
        'botao': 'Cadastrar',
    }


class TipoSolicitacaoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Cadastrar Tipo de Solicitação',
        'botao': 'Cadastrar',
    }


class StatusCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('listar-status')
    extra_context = {
        'titulo': 'Cadastrar Status',
        'botao': 'Cadastrar',
    }


class AlunoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matricula', 'cpf', 'telefone']
    success_url = reverse_lazy('listar-aluno')
    extra_context = {
        'titulo': 'Cadastrar Aluno',
        'botao': 'Cadastrar',
    }


class ServidorCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
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



class HistoricoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('listar-historico')
    extra_context = {
        'titulo': 'Cadastrar Histórico',
        'botao': 'Cadastrar',
    }


##################################################


class CampusUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Atualização de dados do Campus',
        'botao': 'Salvar',
    }


class CursoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Atualização de dados do Curso',
        'botao': 'Salvar',
    }


class TipoSolicitacaoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Atualização de dados do Tipo de Solicitação',
        'botao': 'Salvar',
    }


class StatusUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
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
    # remover o 'solicitado_por' do fields
    fields = ['curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('listar-solicitacao')
    extra_context = {
        'titulo': 'Atualização de dados da Solicitação',
        'botao': 'Salvar',
    }

    # Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        obj = get_object_or_404(Solicitacao, pk=self.kwargs['pk'], solicitado_por=self.request.user)
        return obj


class HistoricoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('listar-historico')
    extra_context = {
        'titulo': 'Atualização de dados do Histórico',
        'botao': 'Salvar',
    }


##################################################


class CampusDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    model = Campus
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-campus')
    extra_context = {
        'titulo': 'Excluir Campus',
        'botao': 'Excluir',
    }


class CursoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    model = Curso
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-curso')
    extra_context = {
        'titulo': 'Excluir Curso',
        'botao': 'Excluir',
    }


class TipoSolicitacaoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-tipo-solicitacao')
    extra_context = {
        'titulo': 'Excluir Tipo de Solicitação',
        'botao': 'Excluir',
    }


class StatusDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
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


class SolicitacaoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-solicitacao')
    extra_context = {
        'titulo': 'Excluir Solicitação',
        'botao': 'Excluir',
    }

    # Alterar o método que busca o objeto pelo ID (get_object)
    def get_object(self, queryset=None):
        obj = get_object_or_404(Solicitacao, pk=self.kwargs['pk'], solicitado_por=self.request.user)
        return obj


class HistoricoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
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


class StatusList(GroupRequiredMixin, ListView):
    group_required = ["Administrador"]
    model = Status
    template_name = 'paginasweb/listas/status.html'


class AlunoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador"]
    model = Aluno
    template_name = 'paginasweb/listas/aluno.html'


class ServidorList(GroupRequiredMixin, ListView):
    group_required = ["Administrador"]
    model = Servidor
    template_name = 'paginasweb/listas/servidor.html'


class SolicitacaoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador"]
    model = Solicitacao
    template_name = 'paginasweb/listas/solicitacao.html'


# Fazer uma herança para ter tudo que tem na SolicitacaoList
class MinhasSolicitacoes(LoginRequiredMixin, ListView):
    model = Solicitacao
    template_name = 'paginasweb/listas/solicitacao.html'
    
    def get_queryset(self):
        # Como fazer consultas/filtros no django
        # Classe.objects.all()  # Retorna todos os objetos
        # Classe.objects.filter(atributio=algum_valor, a2=v2)
        qs = Solicitacao.objects.filter(solicitado_por=self.request.user)
        return qs


class HistoricoList(GroupRequiredMixin, ListView):
    group_required = ["Administrador"]
    model = Historico
    template_name = 'paginasweb/listas/historico.html'
