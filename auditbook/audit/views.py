from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import *
from django.core.paginator import Paginator,EmptyPage
from datetime import datetime
from django.db.models import Avg,Count,Max,Min
from django.db.models.functions import TruncYear
from io import BytesIO
import qrcode
import random
from PIL import Image,ImageDraw,ImageFont



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
            is_super = User.objects.filter(username=user).values('is_superuser').first().get('is_superuser')
            if user:
                auth.login(request,user)
                if is_super == True:
                    return redirect('cms')
                else:
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


def cms(request):
    return render(request,'cms.html',locals())


def logout(request):
    auth.logout(request)
    return redirect('index')


def zhunze(request):
    ac = Stardands.objects.filter(stdclass__icontains='AC').order_by('stdno')
    cnas = Stardands.objects.filter(stdclass__icontains='CNAS').order_by('stdno')
    astm = Stardands.objects.filter(stdclass__icontains='ASTM').order_by('stdno')
    gb = Stardands.objects.filter(stdclass__icontains='GB').order_by('stdno')
    return render(request,'standard.html',locals())

def tixi(request):
    shouce = Zhiliangshouce.objects.filter(fileclass__icontains='质量手册',user=request.user.username).order_by('-xuhao')
    chengxu = Zhiliangshouce.objects.filter(fileclass__icontains='程序文件',user=request.user.username).order_by('shouceno')
    third = Zhiliangshouce.objects.filter(fileclass__icontains='三层次文件',user=request.user.username).order_by('shouceno')
    jishuguanli = Zhiliangshouce.objects.filter(fileclass__icontains='技术管理规定',user=request.user.username).order_by('shouceno')

    #手册分页
    request.session['tim']=datetime.now().strftime('%Y-%M-%D  %H:%M:%S')
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
    return render(request,'personel.html',locals())


def record(request):
    #session时间记录（实验用）
    ret = request.session.get('tim')
    tim = Record.objects.extra(select={"tab_times":"date_format(tabtime,'%%Y')"}).values('tab_times').distinct()
    return render(request,'record.html',locals())

def records(request,tab_time):
    tim = Record.objects.extra(select={"tab_times":"date_format(tabtime,'%%Y')"}).values('tab_times').distinct()
    zhiliang = Record.objects.filter(tabtime__year=tab_time,tabtype__contains='质量记录')
    jishu = Record.objects.filter(tabtime__year=tab_time,tabtype__contains='技术记录')
    ncr = Record.objects.filter(tabtime__year=tab_time,tabtype__contains='NCR')
    nei = Record.objects.filter(tabtime__year=tab_time,tabtype__contains='内审记录')
    return render(request,'records.html',locals())


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
            xuhao = int(Zhiliangshouce.objects.filter(fileclass__icontains='质量手册',user=request.user.username).order_by('-xuhao').values('xuhao').first().get('xuhao'))
            print(xuhao)
            dt = datetime.now()
            num = '%04d-%02d' %(dt.year,dt.month)
            xuhao += 1
            print(xuhao)
            Zhiliangshouce.objects.filter(shouceno=request.POST.get('shouceno')).update(xuhao=xuhao)
            Zhiliangshouce.objects.filter(shouceno=request.POST.get('shouceno')).update(user=request.user.username)
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
        uploadrecord = Records(request.POST,request.FILES)
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




def test_ajax(request):
    ret = request.GET
    print(ret)
    return HttpResponse('OK')


def yanzhm(request):
    data = 'http://www.baidu.com'
    img = qrcode.make(data)      #传入网站计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
    response = HttpResponse(image_stream, content_type="image/jpg")  #将二维码数据返回到页面
    return response

# #验证码
# def valid_code(request):
#     def random_color():
#         return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     img = Image.new('RGB',(100,32),color=random_color())
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.truetype('static/font/DomoAregato Normal.ttf',size=20)
#     valid_code_str = ''
#     for i in range(5):
#         random_no = str(random.randint(0,9))
#         random_low_alpha = chr(random.randint(95,122))
#         random_upper_alpha = chr(random.randint(65,90))
#         random_char = random.choice([random_no,random_low_alpha,random_upper_alpha])
#         draw.text((20*i+2,5),random_char,random_color(),font=font)
#         #保存验证码
#         valid_code_str+=random_char
#     request.session['valid_code_str']=valid_code_str
#     f = BytesIO()
#     img.save(f,'png')
#     data = f.getvalue()
#     return HttpResponse(data)

