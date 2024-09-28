from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User
from django.http import request

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password', 'email', 'first_name', 'last_name','is_staff']

     # Validate if passwords match
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self,validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                is_staff=validated_data['is_staff'],
            )
            user.set_password(validated_data['password'])  # Hash the password
            user.save()
            return user
    
class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by','updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)
    client = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()  # This will return the username

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    

    class Meta:
        model = Project
        fields = ['project_name', 'users']

        
