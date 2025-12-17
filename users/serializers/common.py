from rest_framework import serializers
from ..models import User
from django.contrib.auth import hashers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'bio', 'profile_image']
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None) 
        #  None will prevent an empty confirm_password field on the request not raising an exception

        # Check the passwords match, invalidate if not
        if password != confirm_password:
            raise serializers.ValidationError({
                'confirm_password': 'Passwords do not match.'
            })

        # Hashes password before it's saved
        data['password'] = hashers.make_password(password)

        return data


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','profile_image']