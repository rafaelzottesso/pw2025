from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Aluno, Servidor


# Crie uma classe de formulário para o cadastro de usuários
# A herança é feita para poder tornar o email único e obrigatório
# E outros campos, se necessário
class UsuarioCadastroForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text="Informe um email válido.")

    # Define o model e os fields que vão aparecer na tela
    class Meta:
        model = User
        # Esses dois passwords são para verificar se as senhas são iguais
        fields = ['username', 'email', 'password1', 'password2']

    # O metodo clean no forms serve de validação para os campos
    def clean_email(self):
        # recebe o email do formulário
        email = self.cleaned_data.get('email')
        # Verifica se já existe algum usuário com este email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email


class AlunoCadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um email válido.")
    nome = forms.CharField(max_length=100, required=True, help_text="Informe o nome completo do aluno.")
    matricula = forms.CharField(max_length=100, required=True, help_text="Informe a matrícula do aluno.", label="Matrícula")
    cpf = forms.CharField(max_length=100, required=True, help_text="Informe o CPF do aluno.", label="CPF")
    telefone = forms.CharField(max_length=14, required=True, help_text="Informe o telefone do aluno.")

    class Meta:
        model = User
        fields = ['nome', 'matricula', 'cpf', 'telefone', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if Aluno.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Esta matrícula já está em uso.")
        return matricula

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Aluno.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf


class ServidorCadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um email válido.")
    nome = forms.CharField(max_length=100, required=True, help_text="Informe o nome completo do servidor.")
    siape = forms.CharField(max_length=100, required=True, help_text="Informe o SIAPE do servidor.", label="SIAPE")

    class Meta:
        model = User
        fields = ['nome', 'siape', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_siape(self):
        siape = self.cleaned_data.get('siape')
        if Servidor.objects.filter(siape=siape).exists():
            raise forms.ValidationError("Este SIAPE já está em uso.")
        return siape
