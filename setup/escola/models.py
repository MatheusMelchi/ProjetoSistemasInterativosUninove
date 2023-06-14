from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self) -> str:
        return self.nome
    

class Curso(models.Model):
    NIVEL = {
        ('C', 'Básico'),
        ('B', 'Intermediário'),
        ('A', 'Avancado'),
    }
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=1000)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank= False, null=False, default='C')
    def __str__(self) -> str:
        return self.descricao
    
class Tarefas(models.Model):
    usuario = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=400, null=False)
    data = models.DateField(max_length=10, default='0001-01-01', null=True)
    horario = models.CharField(max_length=10, default='00:00', null=True)
    passo1 = models.CharField(max_length=100, null=True)
    passo2 = models.CharField(max_length=100, null=True)
    passo3 = models.CharField(max_length=100, null=True)
    passo4 = models.CharField(max_length=100, null=True)
    passo5 = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return self.descricao
    
class Usuario(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    foto_perfil = models.ImageField()
    def __str__(self) -> str:
        return self.email
# Create your models here.
