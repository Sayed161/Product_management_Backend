from rest_framework import viewsets
from .models import productsModel
from .serializers import Products_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    queryset = productsModel.objects.all()
    serializer_class = Products_Serializer
    permission_classes = [IsAuthenticated]

  