from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Task
from .serializers import TasksSerializer

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    items = Task.objects.all()
    serializer = TasksSerializer(items, many =True)
    return JsonResponse(serializer.data, safe =False)

def post_task(request):
    pass
