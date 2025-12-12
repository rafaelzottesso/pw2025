from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q, OuterRef, Subquery
from django.db.models.functions import TruncMonth
from paginasweb.models import Solicitacao, Status, TipoSolicitacao, Campus, Curso, Historico
import json


class DashboardRelatoriosView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total de solicitações
        context['total_solicitacoes'] = Solicitacao.objects.count()
        
        # Total de tipos de solicitação
        context['total_tipos'] = TipoSolicitacao.objects.count()
        
        # Total de campus
        context['total_campus'] = Campus.objects.count()
        
        # Total de cursos
        context['total_cursos'] = Curso.objects.count()
        
        return context


class RelatorioSolicitacoesPorStatusView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/solicitacoes_por_status.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Subquery para obter o último histórico de cada solicitação
        ultimo_historico_subquery = Historico.objects.filter(
            solicitacao=OuterRef('pk')
        ).order_by('-cadastrado_em').values('status__nome')[:1]
        
        # Anotar cada solicitação com seu último status
        solicitacoes_com_status = Solicitacao.objects.annotate(
            ultimo_status=Subquery(ultimo_historico_subquery)
        ).values('ultimo_status').annotate(
            total=Count('id')
        )
        
        status_count = {}
        for item in solicitacoes_com_status:
            status_nome = item['ultimo_status'] if item['ultimo_status'] else 'Sem Status'
            status_count[status_nome] = item['total']
        
        # Preparar dados para o gráfico
        context['labels'] = json.dumps(list(status_count.keys()))
        context['values'] = json.dumps(list(status_count.values()))
        context['status_data'] = status_count
        
        return context


class RelatorioSolicitacoesPorTipoView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/solicitacoes_por_tipo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agrupar solicitações por tipo
        tipos_data = Solicitacao.objects.values(
            'tipo_solicitação__descricao'
        ).annotate(
            total=Count('id')
        ).order_by('-total')
        
        labels = [item['tipo_solicitação__descricao'] for item in tipos_data]
        values = [item['total'] for item in tipos_data]
        
        context['labels'] = json.dumps(labels)
        context['values'] = json.dumps(values)
        context['tipos_data'] = tipos_data
        
        return context


class RelatorioSolicitacoesPorCampusView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/solicitacoes_por_campus.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agrupar solicitações por campus através do curso
        campus_data = Solicitacao.objects.values(
            'curso__campus__nome'
        ).annotate(
            total=Count('id')
        ).order_by('-total')
        
        labels = [item['curso__campus__nome'] for item in campus_data]
        values = [item['total'] for item in campus_data]
        
        context['labels'] = json.dumps(labels)
        context['values'] = json.dumps(values)
        context['campus_data'] = campus_data
        
        return context


class RelatorioSolicitacoesPorCursoView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/solicitacoes_por_curso.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agrupar solicitações por curso
        curso_data = Solicitacao.objects.values(
            'curso__nome', 'curso__campus__nome'
        ).annotate(
            total=Count('id')
        ).order_by('-total')[:10]  # Top 10 cursos
        
        labels = [f"{item['curso__nome']} ({item['curso__campus__nome']})" for item in curso_data]
        values = [item['total'] for item in curso_data]
        
        context['labels'] = json.dumps(labels)
        context['values'] = json.dumps(values)
        context['curso_data'] = curso_data
        
        return context


class RelatorioTimelineSolicitacoesView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/timeline_solicitacoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agrupar solicitações por mês, excluindo registros sem data
        timeline_data = Solicitacao.objects.filter(
            cadastrado_em__isnull=False
        ).annotate(
            mes=TruncMonth('cadastrado_em')
        ).values('mes').annotate(
            total=Count('id')
        ).order_by('mes')
        
        # Formatar datas para o gráfico
        labels = [item['mes'].strftime('%b/%Y') if item['mes'] else 'N/A' for item in timeline_data]
        values = [item['total'] for item in timeline_data]
        
        context['labels'] = json.dumps(labels)
        context['values'] = json.dumps(values)
        context['timeline_data'] = timeline_data
        
        return context
