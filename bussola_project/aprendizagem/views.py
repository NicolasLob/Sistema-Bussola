from rest_framework import generics
from .models import Aprendizagem
from .serializers import AprendizagemSerializer

class AprendizagemList(generics.ListAPIView):
    queryset = Aprendizagem.objects.all()  # Busca todos os registros da tabela
    serializer_class = AprendizagemSerializer