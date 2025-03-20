from rest_framework import serializers
from .models import Aprendizagem

class AprendizagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendizagem
        fields = '__all__'  # Inclui todos os campos do modelo