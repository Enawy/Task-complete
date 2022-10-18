from rest_framework import serializers
from client.models import Client
from car.models import Car
from company.models import Company


class Clientserializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class Carserializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
