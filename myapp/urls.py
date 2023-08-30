from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('url',views.url_page),
    path('',views.task_page),
    path('url/task',views.task_page)
]