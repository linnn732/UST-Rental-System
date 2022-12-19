from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
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

#修改會員資料（未更改）
@csrf_exempt
def edit_member(request):

    if request.method == "POST":

        data = request.POST
        
        email = data.get('email')
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        new_tel_number = data.get('tel_number')

        if Member.objects.filter(email=email, password=old_password).exists():
            print("有")
            Member.objects.filter(email=email).update(password=new_password,tel=new_tel_number)
            messages.success(request, "修改成功")
        else:
            print("沒有")
            messages.error(request, "名字或密碼輸入錯誤，請重新輸入")

    return render(request, 'member-nu_edit.html')


def search_nu_site(request):
    context = {}
    if request.method == "POST":
        school = request.POST['school']
        usage = request.POST['usage']
        date = request.POST['date']
        start = int(request.POST['start'])
        end = int(request.POST['end'])

        end_first = start+1
        start_last =end-1

        result = Duration.objects.filter(
        site_id__department_id__school_id = school,
    site_id__usage = usage,
    date = date,
    rent_status = 0,
    start__gte = start,
    start__lte = start_last,
    end__gte = end_first,
    end__lte = end
            )

        context["condition_query_set"] = result
        return render(request, "index.html", context)

    return render(request, "index.html", context)
    
  

    


    