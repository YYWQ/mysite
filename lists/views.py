from django.core.exceptions import ValidationError
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib import auth
from lists.forms import ExistingListItemForm,ItemForm
from lists.models import Item,List

# Create your views here.
#在这儿编写视图

'''#登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #response.set_cookie('user',username, 3600)#添加浏览器cookie
            request.session['user'] = username
            response = redirect(home_page)
            return response
        else:
            return render(request,'login.html',{'error':'username or password error!'})
    else:
        return render(request,'login.html')
'''    
#主页
def home_page(request):
    #username = request.COOKIES.get('user', '')#读取浏览器cookie
    #return render(request,'home.html', {'user':username})
    return render(request,'home.html',{'form': ItemForm()})

def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_,data=request.POST)
        if form.is_valid():
            form.save()
            #Item.objects.create(text=request.POST['text'], list=list_)
            #return redirect(list_)
    return render(request,'list.html',{'list':list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
    
        
    

