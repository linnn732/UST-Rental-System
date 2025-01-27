from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import MemberModelForm, LoginModelForm
from .models import Member
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.


def register(request):
    form = MemberModelForm()
    context = {}
    if request.method == "POST":
        form = MemberModelForm(request.POST, request.FILES)
        if form.is_valid():
            # email = form.cleaned_data['email']
            # print(email)
            form.save()
            context['successful_submit']=True
            #return redirect('register')
    
    context['form']=form

    return render(request, 'register.html', context)

# 會員登入
@csrf_exempt
def login(request):
    form = LoginModelForm()
    context = {}
    if request.method == "POST":
        form = LoginModelForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #email與password是否存在Member table中
            if Member.objects.filter(email=email, password=password).exists():

                #GET Member的name和identity
                member_data = Member.objects.filter(email=email, password=password).values("name","identity")
                context = {
                    'status':'True',
                    'member_data':member_data,
                    'successful_submit':True
                }
                messages.success(request, "登入成功")
                #要改成跳頁
                return HttpResponseRedirect(request.path_info)

            else:
                messages.error(request, "email或密碼輸入錯誤")
                return HttpResponseRedirect(request.path_info)
    
    context['form']=form
    return render(request, 'login.html', context)            


    