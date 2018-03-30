from django.shortcuts import render

# Create your views here.
#在这儿编写视图
def home_page(request):
    return render(request,'home.html')
