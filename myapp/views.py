from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def task_page(request):
	return render(request,"task.html")

def url_page(request):
	return HttpResponse("Hello. Welcome to my Task-1 Django Submission. Go to my task page.")