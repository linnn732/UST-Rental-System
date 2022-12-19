from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Equipment,Department,Member,School,Rent_Equipment
from django.http import HttpResponse,JsonResponse


# 場材管理員查詢器材
@csrf_exempt
def search_se_equ(request):

    data = request.POST
    search_name = data.get('member_name') #前端給會員名稱

    #寫法1
    result = Equipment.objects.filter(
        department_id__school_id__member__name = search_name # 在 Equipment 表中反向查詢 department_id、school_id、member__name
    )

    return_data = result.values_list('id','name','price','amount')
    return JsonResponse(list(return_data),safe=False)
    #return HttpResponse(list(return_data))
    
    
#場財管理員顯示器材租借內容
@csrf_exempt
def generate_rental_equ(request):

    data = request.POST
    search_email = data.get('email')

    result = Rent_Equipment.objects.filter(
        member_id__email = search_email 
    )

    getdata = list(result.values_list('id','date','amount','equipment_id'))
    return_data_list = []
    
    for i in range(len(getdata)):
        rent_id = getdata[i][0] #租借ID
        rent_date = getdata[i][1] #租借日期
        equipment_amount = getdata[i][2] #抓租借數量
        equipment_id = getdata[i][3] #抓器材ID

        equipment_item_data = Equipment.objects.get(id=equipment_id) 
        return_name= equipment_item_data.name #抓器材名字
        return_price=equipment_item_data.price #抓器材價格
        total_price=int(equipment_amount)*int(return_price) #租借總金額（數量乘價格）
        equ_school_name = equipment_item_data.department_id.school_id.name #器材所屬的學校名字

        return_data = rent_id,rent_date,equ_school_name,return_name,equipment_amount,total_price
        return_data_list += {return_data}

    return JsonResponse(return_data_list,safe=False)