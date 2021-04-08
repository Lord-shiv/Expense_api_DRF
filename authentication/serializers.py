from rest_framework import serializers
from .models import User
from django.contrib import auth


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'username should be in alphanumeric character')
        return attrs
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
