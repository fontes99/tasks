from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .serializers import TasksSerializer
from .form import TaskForm

def get_tasks(request):
    items = Task.objects.all()
    serializer = TasksSerializer(items, many =True)
    return JsonResponse(serializer.data, safe =False)

@csrf_exempt
def post_task(request):

    form = TaskForm(request.POST)

    if form.is_valid():
         form.save()
         return JsonResponse(form.data,status = 201)

    return JsonResponse(form.errors,status = 400)
