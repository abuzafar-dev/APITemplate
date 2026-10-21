from rest_framework import serializers

from apps.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_done', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Sarlavha bo'sh bo'lmasin.")
        return value
