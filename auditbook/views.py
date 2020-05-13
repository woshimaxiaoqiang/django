from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import *
from django.core.paginator import Paginator,EmptyPage


def index(request):
    return render(request,'index.html')


def login(request):
    login = Login()
    if request.method=='POST':
        login = Login(request.POST)
        if login.is_valid():
            user = login.cleaned_data.get('user')
            pwd = login.cleaned_data.get('pwd')
            user = auth.authenticate(username=user,password=pwd)
            if user:
                auth.login(request,user)
                next_url = request.GET.get('next','index')
                return redirect(next_url)
            else:
                return render(request,'reg.html')
    else:
        login = login.errors.get('__all__')
        return render(request,'login.html',locals())
    return render(request,'login.html',locals())



def reg(request):
    reg = Reg()
    if request.method=='POST':
        reg = Reg(request.POST)
        if reg.is_valid():
            user = request.POST.get('user')
            pwd = request.POST.get('pwd')
            User.objects.create_user(username=user,password=pwd)
            return redirect('login')
        else:
            error = reg.errors.get('__all__')
            return render(request,'reg.html',locals())
    return render(request,'reg.html',locals())


def logout(request):
    auth.logout(request)
    return redirect('index')


def zhunze(request):
    ac = Stardands.objects.filter(stdclass__icontains='AC').order_by('stdno')
    cnas = Stardands.objects.filter(stdclass__icontains='CNAS').order_by('stdno')
    astm = Stardands.objects.filter(stdclass__icontains='ASTM').order_by('stdno')
    gb = Stardands.objects.filter(stdclass__icontains='GB').order_by('stdno')
    return render(request, 'baogao.html', locals())

def tixi(request):
    shouce = Zhiliangshouce.objects.filter(fileclass__icontains='质量手册').order_by('shouceno')
    chengxu = Zhiliangshouce.objects.filter(fileclass__icontains='程序文件').order_by('shouceno')
    third = Zhiliangshouce.objects.filter(fileclass__icontains='三层次文件').order_by('shouceno')
    jishuguanli = Zhiliangshouce.objects.filter(fileclass__icontains='技术管理规定').order_by('shouceno')
    #手册分页
    shoucefenye = Paginator(shouce,2)
    try:
        shoucecurrent_num = int(request.GET.get('page',1))
        shoucecurrent_page = shoucefenye.page(shoucecurrent_num)
    except EmptyPage as e:
        shoucecurrent_page = shoucefenye.page(1)
    #程序分页
    chengxufenye = Paginator(chengxu,2)
    try:
        chengxucurrent_num = int(request.GET.get('page',1))
        chengxucurrent_page = chengxufenye.page(chengxucurrent_num)
    except EmptyPage as e:
        chengxucurrent_page = chengxufenye.page(1)
    return render(request,'programs.html',locals())

def personel(request):
    leader = Personel.objects.filter(profession__icontains='实验室主任').first()
    zhiliang = Personel.objects.filter(profession__icontains='质量').first()
    jishu = Personel.objects.filter(profession__icontains='技术负责').first()
    qa = Personel.objects.filter(profession__icontains='QA').order_by('name')
    qianziren = Personel.objects.filter(profession__icontains='授权').order_by('name')
    neishen = Personel.objects.filter(profession__icontains='内审').order_by('name')
    chemperson = Personel.objects.filter(profession__icontains='化学').order_by('name')
    phycperson = Personel.objects.filter(profession__icontains='机性').order_by('name')
    jinxperson = Personel.objects.filter(profession__icontains='金相').order_by('name')
    chemequip = Equip.objects.filter(equipfield__icontains='化学').order_by('equipname')
    phyequip = Equip.objects.filter(equipfield__icontains='机性').order_by('equipname')
    jinxequip = Equip.objects.filter(equipfield__icontains='金相').order_by('equipname')
    jilequip = Equip.objects.filter(equipfield__icontains='计量').order_by('equipname')
    elseequip = Equip.objects.filter(equipfield__icontains='其他').order_by('equipname')
    return render(request, 'jilus.html', locals())


def record(request):
    return render(request,'record.html',locals())


def getready(request):
    return render(request,'getready.html',locals())


def addperson(request):
    addperson = Personels
    if request.method=='POST':
        addperson = Personels(request.POST)
        if addperson.is_valid():
            addperson.save()
            return redirect('personel')
    return render(request,'addpersonel.html',locals())


def addequip(request):
    addequip = Equips
    if request.method=='POST':
        addequip = Equips(request.POST)
        if addequip.is_valid():
            addequip.save()
            return redirect('personel')
    return render(request,'addequip.html',locals())


@login_required
def uploadfile(request):
    uploadfile = Uploadfile()
    if request.method=='POST':
        uploadfile = Uploadfile(request.POST,request.FILES)
        if uploadfile.is_valid():
            uploadfile.save()
            return redirect('tixi')
    return render(request,'uploadfile.html',locals())


@login_required
def uploadstd(request):
    uploadstd = Uploadstd()
    if request.method=='POST':
        uploadstd = Uploadstd(request.POST,request.FILES)
        if uploadstd.is_valid():
            uploadstd.save()
            return redirect('zhunze')
    return render(request,'uploadstd.html',locals())


@login_required
def uploadrecord(request):
    uploadrecord = Records()
    if request.method=='POST':
        uploadrecord = Records(request.POST)
        if uploadrecord.is_valid():
            uploadrecord.save()
            return redirect('record')
    return render(request,'uploadrecord.html',locals())


@login_required
def deleteshouce(request,shouceid):
    Zhiliangshouce.objects.filter(id=shouceid).delete()
    return redirect('tixi')


@login_required
def deletestd(request,stdid):
    Stardands.objects.filter(id=stdid).delete()
    return redirect('zhunze')


@login_required
def deleteper(request,perid):
    Personel.objects.filter(id=perid).delete()
    Equip.objects.filter(id=perid).delete()
    return redirect('personel')