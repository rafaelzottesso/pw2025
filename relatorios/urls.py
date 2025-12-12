from django.urls import path
from .views import (
    DashboardRelatoriosView,
    RelatorioSolicitacoesPorStatusView,
    RelatorioSolicitacoesPorTipoView,
    RelatorioSolicitacoesPorCampusView,
    RelatorioSolicitacoesPorCursoView,
    RelatorioTimelineSolicitacoesView,
)

urlpatterns = [
    path('', DashboardRelatoriosView.as_view(), name='relatorios-dashboard'),
    path('solicitacoes-por-status/', RelatorioSolicitacoesPorStatusView.as_view(), name='relatorio-solicitacoes-status'),
    path('solicitacoes-por-tipo/', RelatorioSolicitacoesPorTipoView.as_view(), name='relatorio-solicitacoes-tipo'),
    path('solicitacoes-por-campus/', RelatorioSolicitacoesPorCampusView.as_view(), name='relatorio-solicitacoes-campus'),
    path('solicitacoes-por-curso/', RelatorioSolicitacoesPorCursoView.as_view(), name='relatorio-solicitacoes-curso'),
    path('timeline-solicitacoes/', RelatorioTimelineSolicitacoesView.as_view(), name='relatorio-timeline-solicitacoes'),
]
