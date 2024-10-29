from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O Cpf é invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua numeros no nome"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O campo RG deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O campo celular não é valido 71 11111-3333"})
        return data

    