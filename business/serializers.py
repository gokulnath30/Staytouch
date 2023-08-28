from rest_framework import serializers
from .models import Business
from django.contrib.auth.models import User


class BusinessSerializer(serializers.ModelSerializer):  
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Business
        fields = ('id', 'name', 'description', 'category', 'address','email','phone1','phone2','location','images','ratings','reviews','creator')
    
    # def create(self, validated_data):
    #     user = Business.objects.create(**validated_data)
    #     user.save()
    #     return user


class UserSerializer(serializers.ModelSerializer): 
    business = serializers.PrimaryKeyRelatedField(many=True, queryset=Business.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'business')
