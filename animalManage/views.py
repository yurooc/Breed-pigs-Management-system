import requests
from django.shortcuts import redirect, render
from animal.models import Siliao,Zhongzhu,Peizhong,Renjian,Fenmian,Caijing,Xingweiy
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from animal.models import Site_Info, User
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
import os

# Create your views here.
def index(request):
    return render(request, "animal/index.html")
def xinxiyulan(request):
    return render(request, "animal/xinxiyulan.html")
def xiputu(request):
    return render(request, "animal/xiputu.html")
def shengchantishi(request):
    data1_list = Zhongzhu.objects.filter(Q(peizhong__contains='否')).count()
    data2_list = Zhongzhu.objects.filter(Q(zaizhu__contains='是')).count()
    data3_list = Zhongzhu.objects.filter(pinzhong__contains='种公猪',yimiao__contains='否').count()
    data4_list = Zhongzhu.objects.filter(pinzhong__contains='种母猪', yimiao__contains='否').count()
    return render(request, "animal/shengchantishi.html", {"data1_list": data1_list,"data2_list": data2_list,"data3_list": data3_list,"data4_list": data4_list})


def siliaokucun(request):
    data_list = Siliao.objects.all()
    return render(request, "animal/siliaokucun.html",{'data_list':data_list})
def xingweijilu(request):
    data1_list = Peizhong.objects.all()
    data2_list = Renjian.objects.all()
    data3_list = Fenmian.objects.all()
    data4_list = Caijing.objects.all()
    data5_list = Xingweiy.objects.all()
    return render(request, "animal/xingweijilu.html", {'data1_list': data1_list,'data2_list':data2_list,'data3_list':data3_list,'data4_list':data4_list,'data5_list':data5_list})



def peiadd(request):
    if request.method == "GET":
        return render(request,"animal/peiadd.html")
    bianhao = request.POST.get("bianhao")
    jiluneirong = request.POST.get("jiluneirong")
    Peizhong.objects.create(bianhao=bianhao,jiluneirong=jiluneirong)
    return redirect("/xingweijilu")
def peidelete(request):
    #删除饲料库存
    nid = request.GET.get('nid')
    Peizhong.objects.filter(id=nid).delete()
    return redirect("/xingweijilu")
def renadd(request):
    if request.method == "GET":
        return render(request,"animal/renadd.html")
    bianhao = request.POST.get("bianhao")
    jiluneirong = request.POST.get("jiluneirong")
    Renjian.objects.create(bianhao=bianhao,jiluneirong=jiluneirong)
    return redirect("/xingweijilu")
def rendelete(request):
    nid = request.GET.get('nid')
    Renjian.objects.filter(id=nid).delete()
    return redirect("/xingweijilu")
def fenadd(request):
    if request.method == "GET":
        return render(request,"animal/fenadd.html")
    bianhao = request.POST.get("bianhao")
    jiluneirong = request.POST.get("jiluneirong")
    Fenmian.objects.create(bianhao=bianhao,jiluneirong=jiluneirong)
    return redirect("/xingweijilu")
def fendelete(request):
    nid = request.GET.get('nid')
    Fenmian.objects.filter(id=nid).delete()
    return redirect("/xingweijilu")
def caiadd(request):
    if request.method == "GET":
        return render(request,"animal/caiadd.html")
    bianhao = request.POST.get("bianhao")
    jiluneirong = request.POST.get("jiluneirong")
    Caijing.objects.create(bianhao=bianhao,jiluneirong=jiluneirong)
    return redirect("/xingweijilu")
def caidelete(request):
    nid = request.GET.get('nid')
    Caijing.objects.filter(id=nid).delete()
    return redirect("/xingweijilu")
def yadd(request):
    if request.method == "GET":
        return render(request,"animal/yadd.html")
    bianhao = request.POST.get("bianhao")
    jiluneirong = request.POST.get("jiluneirong")
    Xingweiy.objects.create(bianhao=bianhao,jiluneirong=jiluneirong)
    return redirect("/xingweijilu")
def ydelete(request):
    nid = request.GET.get('nid')
    Xingweiy.objects.filter(id=nid).delete()
    return redirect("/xingweijilu")
def siliaoadd(request):
    if request.method == "GET":
        return render(request,"animal/siliaoadd.html")
    sname = request.POST.get("sname")
    kucun = request.POST.get("kucun")
    Siliao.objects.create(sname=sname,kucun=kucun)
    return redirect("/siliaokucun")
def sdelete(request):
    #删除饲料库存
    nid = request.GET.get('nid')
    Siliao.objects.filter(id=nid).delete()
    return redirect("/siliaokucun")
def edit(request,nid):
    if request.method =="GET":
        row_object = Siliao.objects.filter(id=nid).first()
        print(row_object.sname,row_object.kucun)
        return render(request,'animal/edit.html',{"row_object": row_object})
    #获取
    sname = request.POST.get("sname")
    Siliao.objects.filter(id=nid).update(sname=sname)
    kucun = request.POST.get("kucun")
    Siliao.objects.filter(id=nid).update(kucun=kucun)
    return redirect("/siliaokucun")
def chart_bar(request):
    data1_list = Zhongzhu.objects.filter(Q(zhushe__contains='1')).count()
    data2_list = Zhongzhu.objects.filter(Q(zhushe__contains='2')).count()
    data3_list = Zhongzhu.objects.filter(Q(zhushe__contains='3')).count()
    data4_list = Zhongzhu.objects.filter(Q(zhushe__contains='4')).count()
    data5_list = Zhongzhu.objects.filter(Q(zhushe__contains='5')).count()
    legend = ["数量"]
    series_list =[
        {
            "name": '数量',
            "type": 'bar',
            "data": [data1_list, data2_list, data3_list, data4_list, data5_list]
        }
    ]
    x_axis = ['一号猪舍','二号猪舍','三号猪舍','四号猪舍','五号猪舍']
    result ={
        "status":True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis,
        }
    }
    return JsonResponse(result)
def chart_bing(request):
    data1_list = Zhongzhu.objects.filter(Q(pinzhong__contains='种公猪')).count()
    data2_list = Zhongzhu.objects.filter(Q(pinzhong__contains='种母猪')).count()
    data =[

        { "value": data1_list, "name": '种公猪' },
        { "value": data2_list, "name": '种母猪' },
    ]


    result ={
        "status":True,
        'data':data,

    }
    return JsonResponse(result)
def chart_zong(request):
    data_list = Zhongzhu.objects.all().count()
    data =[
        {
            "value": data_list,
            "name": '种猪数'
        }
    ]
    result ={
        "status":True,
        'data':data
    }
    return JsonResponse(result)
def chart_ku(request):
    data1_list = Siliao.objects.filter(sname='麸皮').values_list('kucun').first()
    data2_list = Siliao.objects.filter(sname='蛋白质类').values_list('kucun').first()
    data3_list = Siliao.objects.filter(sname='矿物质类').values_list('kucun').first()
    data4_list = Siliao.objects.filter(sname='维生素类').values_list('kucun').first()
    data5_list = Siliao.objects.filter(sname='大麦').values_list('kucun').first()
    data6_list = Siliao.objects.filter(sname='小麦').values_list('kucun').first()
    data7_list = Siliao.objects.filter(sname='玉米').values_list('kucun').first()
    data8_list = Siliao.objects.filter(sname='油脂').values_list('kucun').first()
    data =[
        {"value": data1_list, "name": '麸皮'},
        {"value": data2_list, "name": '蛋白质类'},
        {"value": data3_list, "name": '矿物质类'},
        {"value": data4_list, "name": '维生素类'},
        {"value": data5_list, "name": '大麦'},
        {"value": data6_list, "name": '小麦'},
        {"value": data7_list, "name": '玉米'},
        {"value": data8_list, "name": '油脂'}
    ]
    result ={
        "status":True,
        'data':data
    }
    return JsonResponse(result)

def chart_graph(request):

    data_list =[
        {
            "name":1,
            "category": '种公猪',
            "draggable": "true",
        }, {
            "name": 2,
            "category": '种母猪',
            "draggable": "true",
        }, {
            "name": 3,
            "category": '种公猪',
            "draggable": "true",
        }, {
            "name": 4,
            "category": '种母猪',
            "draggable": "true",
        }, {
            "name": 5,
            "category": '种公猪',
            "draggable": "true",
        }, {
            "name": 6,
            "category": '种公猪',
            "draggable": "true",
        }, {
            "name": 7,
            "category": '种母猪',
            "draggable": "true",
        },
    ]
    links =[
        {
            "source": '1',
            "target": '5',
            "value": '父系',

        }, {
            "source": '2',
            "target": '5',
            "value": '母系',
        }, {
            "source": '3',
            "target": '7',
            "value": '父系',
        }, {
            "source": '4',
            "target": '7',
            "value": '母系',
        }, {
            "source": '5',
            "target": '6',
            "value": '父系',
        }, {
            "source": '7',
            "target": '6',
            "value": '母系',
        },
    ]
    result ={
        "status":True,
        'data':{
            'data_list':data_list,
            'links':links,

        }

    }
    return JsonResponse(result)






