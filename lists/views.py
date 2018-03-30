from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#在这儿编写视图
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')

