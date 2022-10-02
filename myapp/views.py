from ast import Delete
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Sum
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
import myapp
from myapp.models import *
from .filters import *
import time
import hashlib
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from Graduation_Topic import func
from django.conf import settings
from django.db import connection, transaction


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # 先設定一個要回傳的message空集合

        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
            print(events)

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            lineId = events[0].source.user_id
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                msg = event.message.text
            if msg[:3] == '###' and len(msg) > 3:  # 購物清單功能
                # func.manageForm(event, msg)
                try:
                    func.manageForm(event, msg, lineId)
                except:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text='發生錯誤！'))
            if msg[:3] == '$$$' and len(msg) > 3:  # 商品查詢功能
                func.select(event, msg)

# ==========================推薦功能============================================

            if event.message.text == "@推薦商品":  # 推薦商品功能
                likezero = cpu.objects.get(id=9)
                likecpu = cpu.objects.get(id=2)
                likemb = MB.objects.get(id=2)
                likessd = ssd.objects.get(id=3)
                likehdd = hdd.objects.get(id=4)
                likedisplay = display.objects.get(id=5)
                likememory = Memory.objects.get(id=6)
                likepower = Power.objects.get(id=7)
                likechassis = chassis.objects.get(id=8)

                lineId = users.objects.filter(
                    linebotId=events[0].source.user_id).exists()  # 取得lineId

                if(lineId):
                    user = users.objects.get(
                        linebotId=events[0].source.user_id)
                    account = user.account
                    result = prs.objects.raw(
                        "SELECT id,account,type,count(*) as 次數 FROM myapp_prs where account = %s group by type order by count(*) desc limit 1;", [account])
                    #  透過以上SQL獲得使用者最高點擊次數的項目
                    print("搜尋筆數為:"+str(len(result)))  # 查詢筆數
                    if len(result) >= 1:
                        print("最高點擊次數為:"+str(result[0].type))
                        print("次數為:"+str(result[0].次數))
                        if len(result) == 0:
                            recommod = likezero
                        elif result[0].type == "Button_cpu":  # 如果是"Button_cpu"推薦預設內容
                            recommod = likecpu
                        elif result[0].type == "Button_mb":
                            recommod = likemb
                        elif result[0].type == "Button_ssd":
                            recommod = likessd
                        elif result[0].type == "Button_hdd":
                            recommod = likehdd
                        elif result[0].type == "Button_display":
                            recommod = likedisplay
                        elif result[0].type == "Button_memory":
                            recommod = likememory
                        elif result[0].type == "Button_power":
                            recommod = likepower
                        else:
                            result[0].type == "Button_chassis"
                            recommod = likechassis
                        try:
                            line_bot_api.reply_message(
                                event.reply_token, FlexSendMessage(
                                    alt_text='推薦結果',
                                    contents={
                                        "type": "bubble",
                                        "hero": {
                                            "type": "image",
                                            "url": str(recommod.pc_images),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": str(recommod.name),
                                                    "size": "lg",
                                                    "wrap": True
                                                },
                                                {
                                                    "type": "separator",
                                                    "color": "#000000"
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "lg",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": str(recommod.commodity),
                                                            "wrap": True,
                                                            "size": "md",
                                                        },


                                                        {
                                                            "type": "text",
                                                            "text": '$' + str(recommod.price),
                                                            "align": "end",
                                                            "size": "xl",
                                                            "weight": "bold",
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "none",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "style": "primary",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "購買連結",
                                                        "uri": str(recommod.url_list)
                                                    }
                                                }
                                            ],
                                            "flex": 0,
                                            "margin": "xs"
                                        }
                                    }
                                ))
                        except:
                            line_bot_api.reply_message(
                                event.reply_token, TextSendMessage(text='發生錯誤！'))
                else:
                    reply_arr = []
                    # line_bot_api.reply_message(
                    #     event.reply_token, TextSendMessage(text='https://joblinebotapp.herokuapp.com/bind/%s/' % events[0].source.user_id))
                    url = 'https://gproject-app.fly.dev/bind/%s/' % events[0].source.user_id
                    reply_arr.append(FlexSendMessage(
                        alt_text='搜尋結果',
                        contents={
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "查無資料!",
                                        "weight": "bold",
                                        "color": "#1DB446",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "綁定Line",
                                        "weight": "bold",
                                        "size": "xl",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#000000",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "前往綁定",
                                            "uri": url
                                        },
                                        "style": "primary",
                                        "margin": "lg"
                                    },
                                    {
                                        "type": "text",
                                        "text": "沒有帳號?",
                                        "weight": "bold",
                                        "size": "xl",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#000000"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "前往註冊",
                                            "uri": "https://gproject-app.fly.dev/signup/"
                                        },
                                        "style": "secondary",
                                        "margin": "md"
                                    }
                                ]
                            },
                            "styles": {
                                "footer": {
                                    "separator": True
                                }
                            }
                        }
                    ))
                    line_bot_api.reply_message(  # 回覆訊息
                        event.reply_token, reply_arr
                    )

        return HttpResponse()

    else:
        return HttpResponseBadRequest()


def form(request):
    intel = cpu.objects.filter(vendor='intel')[:10]
    amd = cpu.objects.filter(vendor='AMD')[:10]
    mb_1 = MB.objects.filter(vendor='華碩')[:7]
    mb_2 = MB.objects.filter(vendor='技嘉')[:7]
    mb_3 = MB.objects.filter(vendor='微星')[:7]
    ssd1 = ssd.objects.filter(vendor='三星')[:7]
    ssd2 = ssd.objects.filter(vendor='WD')[:7]
    ssd3 = ssd.objects.filter(vendor='金士頓')[:7]
    hdd1 = hdd.objects.filter(vendor='東芝Toshibe')[:7]
    hdd2 = hdd.objects.filter(vendor='WD')[:7]
    hdd3 = hdd.objects.filter(vendor='希捷Seagate')[:7]
    display1 = display.objects.filter(vendor='MSI 微星')[:7]
    display2 = display.objects.filter(vendor='華碩')[:7]
    display3 = display.objects.filter(vendor='技嘉')[:7]
    Memory1 = Memory.objects.filter(vendor='威剛ADATA')[:7]
    Memory2 = Memory.objects.filter(vendor='巨蟒ANACOMDA')[:7]
    Memory3 = Memory.objects.filter(vendor='宇瞻Apacer')[:7]
    Power1 = Power.objects.filter(vendor='CORSAIR 海盜船')[:7]
    Power2 = Power.objects.filter(vendor='Cooler Master')[:7]
    Power3 = Power.objects.filter(vendor='ASUS 華碩')[:7]
    chassis1 = chassis.objects.filter(vendor='ABKONCORE')[:7]
    chassis2 = chassis.objects.filter(vendor='Antec安鈦克')[:7]
    chassis3 = chassis.objects.filter(vendor='ASUS華碩')[:7]
    return render(request, 'form.html', locals())


def configure(request, key, formid):
    data = db.objects.filter(lineID=key) & db.objects.filter(formID=formid)
    return render(request, 'configure.html', locals())


def index(request):
    # request.session.clear()

    return render(request, 'index.html', locals())

# ======商品列表===========================================================================


def CPU(request):

    cpu_all = cpu.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    all_count = All.objects.all().count()
    cpu_Filter = cpuFilter(queryset=cpu_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        try:
            name = request.POST['search']
            namelike1 = '%' + name + '%'
            namelike2 = name + '%'
            namelike3 = '%' + name
            result = All.objects.raw(
                "select * from myapp_all where name like %s or name like %s or name like %s", [namelike1, namelike2, namelike3])
            showData = result
            count = 0
            for i in showData:
                count += 1
            print(count)

        except:
            pass
        cpu_Filter = cpuFilter(request.POST, queryset=cpu_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'cpu_Filter': cpu_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'cpu.html', locals())


def HDD(request):
    hdd_all = hdd.objects.all()  # 變數=model的資料表
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    hdd_Filter = hddFilter(queryset=hdd_all)
    All_Filter = ALLFilter(queryset=All_data)
    hdd_Filter = hddFilter(request.POST, queryset=hdd_all)
    All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'hdd_Filter': hdd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'hdd.html', locals())


def SSD(request):
    ssd_all = ssd.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    ssd_Filter = ssdFilter(queryset=ssd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        ssd_Filter = ssdFilter(request.POST, queryset=ssd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'ssd_Filter': ssd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'ssd.html', locals())


def Display(request):
    display_all = display.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    display_Filter = displayFilter(queryset=display_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        display_Filter = displayFilter(request.POST, queryset=display_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'display_Filter': display_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'display.html', locals())


def Chassis(request):
    chassis_all = chassis.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    chassis_Filter = displayFilter(queryset=chassis_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        chassis_Filter = displayFilter(request.POST, queryset=chassis_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'chassis_Filter': chassis_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'chassis.html', locals())


def manager(request):
    cursor = connection.cursor()
    if(request.session["token"] != True):
        return redirect('/login')
    products = All.objects.all()
    select = 'myapp_all'
    if request.method == "POST":
        try:
            select = request.POST['select']
            if(select == 'myapp_all'):
                showProduct = ''
            else:
                sql = "select * from " + str(select)
                result = All.objects.raw(sql)
                showProduct = result
                # columns = showProduct.columns
                # cursor.execute(sql)
                # showProduct = cursor.fetchall()
                # test = []
                # for i in showProduct:
                #     test.append(i)
                # print(test[1][2])
                option = select.split('_')
        except:
            pass
        try:
            delete = request.POST['del']
            delete = delete.split('&')
            if(delete[1] == 'myapp_all'):
                All.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_cpu'):
                cpu.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_ssd'):
                ssd.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_display'):
                display.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_chassis'):
                chassis.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_hdd'):
                hdd.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_mb'):
                MB.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_memory'):
                Memory.objects.filter(id=delete[0]).delete()
            elif(delete[1] == 'myapp_power'):
                Power.objects.filter(id=delete[0]).delete()
            products = All.objects.all()
        except:
            pass
        try:
            name = request.POST['search']
            namelike1 = '%' + name + '%'
            namelike2 = name + '%'
            namelike3 = '%' + name
            result = All.objects.raw(
                "select * from myapp_all where name_all like %s or name_all like %s or name_all like %s", [namelike1, namelike2, namelike3])
            products = result
        except:
            pass
    return render(request, 'Manager.html', locals())


def adminLogout(request):
    request.session["token"] = False
    return redirect('/')


def update(request, table, key):
    table = table
    sql = 'select * from ' + str(table) + ' where id=' + str(key)
    data = All.objects.raw(sql)
    if request.method == "POST":
        name = request.POST['product_name']
        vendor = request.POST['product_vendor']
        price = request.POST['product_price']
        image = request.POST['product_image']
        url = request.POST['product_url']
        if(table == 'myapp_all'):
            All.objects.filter(id=key).update(
                name_all=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_cpu'):
            cpu.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_ssd'):
            ssd.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_display'):
            display.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_chassis'):
            chassis.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_hdd'):
            hdd.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_mb'):
            MB.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_memory'):
            Memory.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        elif(table == 'myapp_power'):
            Power.objects.filter(id=key).update(
                name=name, vendor=vendor, price=price, url_list=url, pc_images=image
            )
        sql = 'select * from ' + str(table) + ' where id=' + str(key)
        data = All.objects.raw(sql)

    return render(request, 'update.html', locals())
# ===========登入、註冊============================


def Signup(request):
    if request.method == "POST":
        ID = request.POST['ID']
        mail = request.POST['mail']
        password = request.POST['password']
        password1 = request.POST['password1']

        name = request.POST['name']
        sex = request.POST['rdo']
        if sex == "man":
            sex = True
        elif sex == "woman":
            sex = False
        if password != password1:
            messages = "請輸入相同密碼"
        else:
            if users.objects.filter(account=ID).exists():
                messages = "帳號已建立!"
            elif not users.objects.filter(account=ID).exists():
                user = users.objects.create(
                    account=ID, username=name, email=mail, password=password, sex=sex)
                user.save()
                messages = "註冊成功"

    return render(request, 'signup.html', locals())


def Login(request):

    if request.method == 'POST':
        ID = request.POST['username']
        userpassword = request.POST['password']
        if(ID == 'admin' and userpassword == 'admin'):
            request.session["token"] = True
            return redirect('/manager')
        else:
            user = users.objects.filter(
                account=ID, password=userpassword).exists()  # 比對帳號密碼
            print(user)
            if user == False:
                messages = "登入失敗請確認帳號或密碼"
                request.session["verify"] = False
            else:
                request.session["verify"] = True
                name = users.objects.filter(account=ID)  # 比對帳號
                for name in name:
                    request.session["yourname"] = name.username
                    request.session["account"] = name.account
                return redirect('/aftlogin')

    return render(request, 'login.html', locals())


def bind(request, key=None):

    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['password']

        print(account)
        print(password)

        user = users.objects.filter(
            account=account, password=password).exists()  # 比對帳號密碼
        if user == False:
            messages = "綁定失敗請確認帳號或密碼"
        else:
            messages = "綁定成功!!"
            request.session['id'] = key
            print(request.session['id'])
            users.objects.filter(account=account).update(
                linebotId=request.session['id']
            )

    return render(request, 'bind.html', locals())


# 登入後====================================================================

def aftlogin(request):
    verify = request.session["verify"]
    print(verify)
    print("debug", verify)
    # ======預設推薦
    likezero = cpu.objects.get(id=9)
    likecpu = cpu.objects.get(id=2)
    likemb = MB.objects.get(id=2)
    likessd = ssd.objects.get(id=3)
    likehdd = hdd.objects.get(id=4)
    likedisplay = display.objects.get(id=5)
    likememory = Memory.objects.get(id=6)
    likepower = Power.objects.get(id=7)
    likechassis = chassis.objects.get(id=8)

    if verify == True:
        yourname = request.session["yourname"]
        account = request.session["account"]
        print(request.session["yourname"])

        result = prs.objects.raw(
            "SELECT id,account,type,count(*) as 次數 FROM myapp_prs where account = %s group by type order by count(*) desc limit 1;", [account])
        #  透過以上SQL獲得使用者最高點擊次數的項目
        if len(result) > 1:
            print("搜尋筆數為:"+str(len(result)))  # 查詢筆數
            print("最高點擊次數為:"+str(result[0].type))
            print("次數為:"+str(result[0].次數))

        if len(result) == 0:
            recommod = likezero
        elif result[0].type == "Button_cpu":  # 如果是"Button_cpu"推薦預設內容
            recommod = likecpu
        elif result[0].type == "Button_mb":
            recommod = likemb
        elif result[0].type == "Button_ssd":
            recommod = likessd
        elif result[0].type == "Button_hdd":
            recommod = likehdd
        elif result[0].type == "Button_display":
            recommod = likedisplay
        elif result[0].type == "Button_memory":
            recommod = likememory
        elif result[0].type == "Button_power":
            recommod = likepower
        else:
            result[0].type == "Button_chassis"
            recommod = likechassis
    else:
        yourname = "尚未登入"
    return render(request, 'aftlogin.html', locals())


def MB1(request):
    mb_all = MB.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    mb_Filter = displayFilter(queryset=mb_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        mb_Filter = displayFilter(request.POST, queryset=mb_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'mb_Filter': mb_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'MB.html', locals())


def Memory1(request):
    memory_all = Memory.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    memory_Filter = displayFilter(queryset=memory_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        memory_Filter = displayFilter(request.POST, queryset=memory_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'memory_Filter': memory_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'Memory.html', locals())


def Power1(request):
    power_all = Power.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    power_Filter = displayFilter(queryset=power_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        power_Filter = displayFilter(request.POST, queryset=power_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'power_Filter': power_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'Power.html', locals())


def otcpu(request):
    cpu_all = cpu.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_cpu = prs.objects.create(
            account=account, type="Button_cpu", time=localtime)
        save_cpu.save()
    else:
        yourname = "尚未登入"

    print("購物車"+str(cart))
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        print('成功！')
        username = request.session["yourname"]
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料

    cpu_Filter = cpuFilter(queryset=cpu_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        cpu_Filter = cpuFilter(request.POST, queryset=cpu_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'cpu_Filter': cpu_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'otcpu.html', locals())


def otchassis(request):
    username = request.session["yourname"]
    chassis_all = chassis.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_chassis = prs.objects.create(
            account=account, type="Button_chassis", time=localtime)
        save_chassis.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    chassis_Filter = displayFilter(queryset=chassis_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        chassis_Filter = displayFilter(request.POST, queryset=chassis_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'chassis_Filter': chassis_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otchassis.html', locals())


def otdisplay(request):
    username = request.session["yourname"]
    display_all = display.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_display = prs.objects.create(
            account=account, type="Button_display", time=localtime)
        save_display.save()
    else:
        yourname = "尚未登入"

    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    display_Filter = displayFilter(queryset=display_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        display_Filter = displayFilter(request.POST, queryset=display_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'display_Filter': display_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'otdisplay.html', locals())


def othdd(request):
    username = request.session["yourname"]
    hdd_all = hdd.objects.all()  # 變數=model的資料表
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_hdd = prs.objects.create(
            account=account, type="Button_hdd", time=localtime)
        save_hdd.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    hdd_Filter = hddFilter(queryset=hdd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        hdd_Filter = hddFilter(request.POST, queryset=hdd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'hdd_Filter': hdd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'othdd.html', locals())


def otMB(request):
    username = request.session["yourname"]
    mb_all = MB.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_mb = prs.objects.create(
            account=account, type="Button_mb", time=localtime)
        save_mb.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    mb_Filter = displayFilter(queryset=mb_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        mb_Filter = displayFilter(request.POST, queryset=mb_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'mb_Filter': mb_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otMB.html', locals())


def otPower(request):
    username = request.session["yourname"]
    power_all = Power.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_power = prs.objects.create(
            account=account, type="Button_power", time=localtime)
        save_power.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    power_Filter = displayFilter(queryset=power_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        power_Filter = displayFilter(request.POST, queryset=power_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'power_Filter': power_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otPower.html', locals())


def otssd(request):
    username = request.session["yourname"]
    ssd_all = ssd.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_ssd = prs.objects.create(
            account=account, type="Button_ssd", time=localtime)
        save_ssd.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    ssd_Filter = ssdFilter(queryset=ssd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        ssd_Filter = ssdFilter(request.POST, queryset=ssd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'ssd_Filter': ssd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otssd.html', locals())


def otMemory(request):
    username = request.session["yourname"]
    memory_all = Memory.objects.all()
    All_data = All.objects.all()
    All_data_count = All.objects.all().count()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_memory = prs.objects.create(
            account=account, type="Button_memory", time=localtime)
        save_memory.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.filter(name_all=cart).first()
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images, user=username)  # 新增資料

        save_cartdb.save()  # 儲存資料
    memory_Filter = displayFilter(queryset=memory_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        memory_Filter = displayFilter(request.POST, queryset=memory_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'memory_Filter': memory_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otMemory.html', locals())


def CART(request):  # 購物清單
    username = request.session["yourname"]
    cursor = connection.cursor()
    cart_all = cartdb.objects.raw(
        "select * from myapp_cartdb where user = %s", [username])
    #total = cartdb.objects.aggregate(Sum('price'))
    total = 0
    for i in cart_all:
        total += i.price
    finalTotal = total
    print(finalTotal)

    if request.method == "POST":
        cart_result = request.POST.get('cart_del')
        defbutton = request.POST.get('button')

        # print("全部刪除按鈕"+str(defbutton))
        # print("刪除按鈕"+str(cart_result))
        if defbutton == 'Yes':
            cursor.execute(
                "DELETE from myapp_cartdb where user=%s", [username])
            finalTotal = 0
            cart_all = cartdb.objects.raw(
                "select * from myapp_cartdb where user = %s", [username])
        else:
            pass
        if cart_result != 'NO' and cartdb.objects.filter(name=cart_result).exists():
            product_del = cartdb.objects.filter(name=cart_result).first()
            product_del.delete()
            # cursor.execute(
            #     "DELETE from myapp_cartdb where name=%s limit1", [cart_result])
            cart_all = cartdb.objects.raw(
                "select * from myapp_cartdb where user = %s", [username])
            total = 0
            for i in cart_all:
                total += i.price
                print(total)
            finalTotal = total
            print('刪除後'+str(finalTotal))

    return render(request, "cart.html", locals())
# Create your views here.
