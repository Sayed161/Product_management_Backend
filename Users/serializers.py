from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=[choice for choice in User.role_choices if choice[0] != 'admin'])  # Exclude 'admin' role

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'role']

    def validate(self, data):
        """
        Validate password confirmation.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'error': "Passwords do not match"})
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance.
        """
        validated_data.pop('confirm_password')
        role = validated_data.pop('role', 'Seller')  
        user = User.objects.create_user(role=role, **validated_data)
        return user




class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']



