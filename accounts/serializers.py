from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'created_at',)
        read_only_fields = ('created_at',)
