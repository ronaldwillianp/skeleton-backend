from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group, Permission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups_d = GroupSerializer(many=True, read_only=True, source='groups')

    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'groups', 'groups_d']
        # Hace que el campo password no sea visible desde la vista
        extra_kwargs = {'password': {'write_only': True}, 'groups': {'write_only': True}}

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['id'] = str(user.id)
        token['username'] = str(user.username)
        token['first_name'] = str(user.first_name)
        token['last_name'] = str(user.last_name)
        token['is_staff'] = user.is_staff
        token['email'] = user.email
        token['groups'] = list(Group.objects.filter(user=user).values('id','name'))
        return token

