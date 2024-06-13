from rest_framework import serializers

from main.models import Statement, Dormitory, Email


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = "__all__"


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = "__all__"


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
    recipient = serializers.EmailField()

    def create(self, validated_data):
        return Email(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.save()
        return instance
