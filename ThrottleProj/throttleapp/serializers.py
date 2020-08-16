from rest_framework import serializers
from .models import UserModel, ActivityPeriodModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = ['real_name']
        fields = '__all__'


class ActivityPeriodSerializer(serializers.ModelSerializer):
    users_sez = UserSerializer(read_only=True, many=True)

    class Meta:
        model = ActivityPeriodModel
        # fields = ['real_name']
        fields = '__all__'
        # depth = 1
