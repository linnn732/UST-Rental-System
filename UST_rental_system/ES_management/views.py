from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

def add_equ(request):
    #取得post data
    
    form = AddEquModelForm()
    context = {}
    if request.method == "POST":
        form = AddEquModelForm(request.POST)
        if form.is_valid():

            form.save()
  
    context['form']=form

    return render(request, 'add_equipment.html', context)

    # name = request.POST.get('name')
    # usage = request.POST.get('usage')
    # amount = request.POST.get('amount')
    # price = request.POST.get('price')
    # picture = request.POST.get('picture')
    # email = request.POST.get('email')
    
    # #從 email 抓 department_id
    # em  = Member.objects.get(email=email)  
    # emm = Member.objects.filter(email=em.email).values('id','name','email','school_id')  
    
    # for em in emm:
    #     queryset = Department.objects.filter(email=em['email'],school_id=em['school_id']).values('id') #'date','amount','return_address','state','timestamp','equipment_id'
    #     em['department_id'] = list(queryset)
        

    # Equipment.objects.create(name=name, usage=usage, amount=amount, price=price,picture=picture,department_id=Department(em['department_id'][0]['id']) )
    
    
    # return render(".html",content)

@csrf_exempt
def update_equ(request):

    if request.method == "POST":

        data = request.POST

        name = data.get('name')
        usage = data.get('usage')
        price = data.get('price')
        picture = data.get('picture')
        amount = data.get('amount')

        if Equipment.objects.filter(name=name,).exists(): #到時用 id 去改
            print("有")
            Equipment.objects.filter(name=name).update(usage=usage,price=price,picture=picture,amount=amount) #到時新增 update name
            messages.success(request, "修改成功")
        else:
            print("沒有")
            messages.error(request, "修改失敗")

    return render(request, 'equipment_edit.html')