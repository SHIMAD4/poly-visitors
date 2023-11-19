from rest_framework import serializers

from main.models import Statement, Dormitory


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = '__all__'
