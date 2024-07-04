from rest_framework import serializers
from .models import productsModel

class Products_Serializer(serializers.ModelSerializer):
    class Meta:
        model = productsModel
        fields = '__all__'
    def get_created_by_role(self, obj):
        return obj.Created_by.role