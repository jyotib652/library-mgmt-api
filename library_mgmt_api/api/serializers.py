
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import update_last_login

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Book, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id', 'email', 'password', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class BookRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'first_name', 'last_name', 'role']


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('email', 'password', 'password2', 'first_name', 'last_name', 'role')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs

  def create(self, validated_data):
    user = User.objects.create(
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      role = validated_data['role']
    )
    if validated_data['role'] == 1:
        user.is_staff = True
        user.is_librarian = True
    if validated_data['role'] == 2:
        user.is_member = True

    user.set_password(validated_data['password'])
    user.save()

    return user




