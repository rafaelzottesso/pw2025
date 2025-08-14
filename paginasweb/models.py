from django.db import models

# import User
from django.contrib.auth.models import User

# Todas as classes DEVEM ter a herança para a classe Model que está dentro de "models"
# class SuaClasse(models.Model):
#   atributo = models.TipoDeAtributo(propriedade1=valor1, p2="v2", p3=v3)

# Depois de criar as classes, defina os atributos e seus tipos
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-types

# Cada campo tem suas propriedades, que estão disponíveis em
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-options


class Campus(models.Model):
    nome = models.CharField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    # Texto que vai aparecer no select de outras classes, como no cadastro de Curso, por exemplo.
    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        ordering = ['nome']


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.campus})"
    
    class Meta:
        ordering = ['nome', 'campus']


class TipoSolicitacao(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    prazo_externo = models.CharField(max_length=250)
    prazo_externo_dias = models.PositiveSmallIntegerField(default=0, help_text="Informe o prazo em dias que a solicitação leva para ser resolvida.")
    prazo_interno = models.CharField(max_length=250)
    prazo_interno_dias = models.PositiveSmallIntegerField(default=0)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    
    class Meta:
        ordering = ['descricao']


class Status(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.PositiveSmallIntegerField()
    pode_editar = models.BooleanField(help_text="Marque essa opção se for permitido atualizar a solicição com este Status.")
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ordem} - {self.nome}"
    
    class Meta:
        ordering = ['ordem']


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
    
    class Meta:
        ordering = ['nome', 'matricula']


class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    siape = models.CharField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='servidor')

    def __str__(self):
        return f"{self.nome} ({self.siape})"
    
    class Meta:
        ordering = ['nome', 'siape']


class Solicitacao(models.Model):
    solicitado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    turma = models.CharField(max_length=100)
    tipo_solicitação = models.ForeignKey(TipoSolicitacao, on_delete=models.PROTECT)
    justificativa = models.TextField()
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.pk} - {self.tipo_solicitação}"
    
    class Meta:
        ordering = ['-cadastrado_em']


class Historico(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.solicitacao} - {self.status}"
    
    class Meta:
        ordering = ['-cadastrado_em']