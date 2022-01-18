from rest_framework import serializers
from django.contrib.auth.models import User
from .models import*

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class FileModelSerializer(serializers.ModelSerializer):
    def validate_uploaded_file(self, value):
        """
        Check that the uploaded file in the request is valid.
        """
        if not value.name.endswith('.json'):
            raise serializers.ValidationError("Invalid File type")
        return value
    
    class Meta:
        model = FileModel
        fields = '__all__'


class PostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostData
        fields = '__all__'        