from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import Client
from car.models import Car
from company.models import Company
from .serializers import Clientserializer, Carserializer, Companyserializer


@api_view(['GET'])
def getclient(request):
    test = Client.objects.all()
    serializer = Clientserializer(test, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getcar(request):
    test = Car.objects.all()
    serializer = Carserializer(test, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getcompany(request):
    test = Company.objects.all()
    serializer = Companyserializer(test, many=True)
    return Response(serializer.data)
