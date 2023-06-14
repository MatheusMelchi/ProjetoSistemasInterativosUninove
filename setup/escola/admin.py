from django.contrib import admin
from escola.models import Aluno, Curso, Tarefas, Usuario

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    
admin.site.register(Aluno, Alunos)
    
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20
    
admin.site.register(Curso, Cursos)

class TarefasDisplay(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'descricao', 'passo1', 'passo2', 'passo3', 'passo4', 'passo5')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 100
    
admin.site.register(Tarefas, TarefasDisplay)

class Usuarios(admin.ModelAdmin):
    list_display = ('email', 'usuario')
    list_display_links = ('email', 'usuario')
    search_fields = ('email',)
    list_per_page = 100
# Register your models here.
