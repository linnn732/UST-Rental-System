from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Member
from django.core import serializers
from django.http import HttpResponse,JsonResponse


# 系統管理員查詢會員資料
@csrf_exempt
def search_member(request):

    context = {}


    filter_obj = list(Member.objects.all().values('id','name','email','identity','sex','birthday','tel'))
    context["member_set"] = filter_obj
    #return JsonResponse(filter_obj, safe=False)
    return render(request, 'member_manage.html',context)




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
