from rest_framework import serializers

from main.models import Statement, Dormitory


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ('title', 'payment', 'status', 'date', 'file', 'student')


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ('title', 'street', 'student', 'commandant')
