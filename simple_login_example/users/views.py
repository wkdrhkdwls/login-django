from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User

# Create your views here.


def login(request):
    context = {
        'method': request.method,
        'is_valid': True
    }

    if (request.method == 'GET'):
        return render(request, 'users/login.html', context)

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)

            response = redirect('pages:index')
            response.set_cookie('is_login', True)
            response.set_cookie('username', user.username)
            response.set_cookie('password', user.password)

            return response
        except User.DoesNotExist:
            context['is_valid'] = False
        return render(request, 'users/login.html', context)


def signup(request):
    context={
        'blank':False,
        'exists':False,
    }
    template_name="users/signup.html"
    
    if request.method == "GET":
        return render(request, template_name,context)
    
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        #추가할 코드
        user = User.objects.create(username=username,password=password)
        
        if username == "" or password=="":
            context['blank']= True
            return render(request,template_name,context)
        
        exist = User.objects.filter(username=username).exists()
        if exist:
            context['exists'] = exist
            return render(request,template_name,context)
        
        
        #====
        return redirect("pages:index")
    
def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')

def index(request,):
    return render(request, 'index.html')

def logout(request):
    response = redirect('pages:index')
    response.delete_cookie('is_login')
    response.delete_cookie('username')
    response.delete_cookie('password')
    
    return response