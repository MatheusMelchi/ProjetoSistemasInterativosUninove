from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from escola.models import Aluno, Curso, Tarefas, Usuario
from escola.serializer import AlunoSerializer, CursoSerializer, TarefasSerializer, UsuarioSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TarefasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Tarefas"""
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def GetUsuarioByEmail(request, email):
    usuario = Usuario.objects.get(email=email)
    return JsonResponse(usuario)

def alunos(resquest):
    if resquest.method == 'GET':
        aluno = {'id': 1, 'nome':'Guilherme'}
        return JsonResponse(aluno)


# Create your views here.
