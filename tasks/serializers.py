from rest_framework.serializers import ModelSerializer

from .models import Task

class TasksSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'pub_date', 'description')
