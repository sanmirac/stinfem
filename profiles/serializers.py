from rest_framework import serializers

from profiles.models import User, Student, Teacher, Parent


class AuthenticationSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
