from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_tasks, name='get'),
    path('post', views.post_task, name='post'),
]
