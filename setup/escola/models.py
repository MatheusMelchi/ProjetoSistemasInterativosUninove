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
    usuario = models.CharField(max_length=20)
    descricao = models.CharField(max_length=400, null=False)
    data = models.DateField(max_length=10, default='0000')
    horario = models.CharField(max_length=10, default='00:00')
    passo1 = models.CharField(max_length=100)
    passo2 = models.CharField(max_length=100)
    passo3 = models.CharField(max_length=100)
    passo4 = models.CharField(max_length=100)
    passo5 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.descricao
# Create your models here.
