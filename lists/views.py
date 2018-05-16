from django.core.exceptions import ValidationError
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib import auth
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
    return render(request,'home.html')

def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id,))
        except ValidationError:
            error = "You can't have an empty list item"
            
    return render(request,'list.html',{'list':list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'],list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id,))

