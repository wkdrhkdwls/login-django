from django.shortcuts import render
from django.http import HttpResponse
import json
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def login(request):
    user_data = {
        'username':'python',
        'password' : 'django'
    }
    
    if(request.method == "GET"):
        return render(request, 'users/login.html')
    
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        #blank 상태일 때는, 유저가 input을 입력하지않고 제출했을 때(유저가 실수했을떄)
        if username=='':
            return HttpResponse('유저 아이디를 입력해주세요')
        if password=='':
            return HttpResponse('유저 비밀번호를 입력해주세요')
        
        if(username != user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')
        if(password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
        
        return HttpResponse('로그인 성공!')
    
    # data = json.dumps(request.GET) # 딕셔너리를 문자로 바꿔줘야함 = json.dumps
    # return HttpResponse(data)

def login_detail(request,id):
    return HttpResponse('user id는 '+str(id)+'입니다.')