from django.contrib import admin  # Adicione esta linha
from django.urls import path
from aprendizagem.views import AprendizagemList  # Importe a view da API

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração do Django
    path('api/aprendizagem/', AprendizagemList.as_view(), name='aprendizagem-list'),  # Rota da API
]