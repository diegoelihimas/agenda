#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#habilitar o devjango no settings projetc interpreter
#run e depois edit configurations (runserver)
# python manage.py migrate (criar tabelas)
# (criar usuario)python manage.py createsuperuser --username admin
#migrate (migra para o banco de dados), migrations cria um arquivo de migração #sqlmigrate manualmente
# add "core" em settings installed apps
#python manage.py makemigrations core
#python manage.py sqlmigrate core 0001
#admin.site.register(Evento) em admin para tabela
 #
 # class Meta: nome da tabela
 #        db_table = "evento" #nome da tabela
 #
 #    def __str__(self): titulo do evento
 #        return self.titulo

# em admin.py
# class EventoAdmin(admin.ModelAdmin):
#     list_dislay = ("titulo", "data_evento", "data_criacao")
#
#
# admin.site.register(Evento, EventoAdmin)

# class Evento(models.Model):
#     titulo = models.CharField(max_length=100)
#     descricao = models.TextField(blank=True, null=True)
#     data_evento = models.DateTimeField(verbose_name= "data do evento") #nome na tabela
#     data_criacao = models.DateTimeField(auto_now=True)
#         usuario = models.ForeignKey(User, on_delete=models.CASCADE())
#     class Meta:
#         db_table = "evento" #nome da tabela
#
#     def __str__(self):
#         return self.titulo

#criar pasta template botao direito no projeto new directory
#botao direito no template new file HTML5
#views def
#url criar rota
# #agenda settings registrar templates
#     def __str__(self):
#         return self.titulo
#
#     def get_data_criacao(self): formato brasileiro
#         return self.data_evento.strftime("%d/%m/%Y")
# Em agenda!!
# <ul>
#         {%for evento in eventos %}
#         <li> {{evento.titulo}} - {{evento.get_data_evento}}</li>
#         {% endfor %}
#     </ul>
