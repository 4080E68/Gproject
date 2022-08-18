from django.db import models

# Create your models here.


class All(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name_all = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址


class display(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")  # 詳細資訊
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    display_chip = models.CharField(max_length=255, default="")  # 顯示晶片
    Memory = models.CharField(max_length=255, default="")  # 記憶體


class cpu (models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    chip = models.CharField(max_length=255, default="")  # 核心
    thread = models.CharField(max_length=255, default="")  # 執行緒
    speed = models.CharField(max_length=255, default="")  # 時脈速度
    foot_position_cpu = models.CharField(max_length=255, default="")  # 腳位


class ssd(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    capacity_TB = models.FloatField(max_length=255, default="0.0")  # 容量
    size = models.CharField(max_length=255, default="")  # 尺寸
    read_speed_mbs = models.IntegerField(default="")  # 讀取
    write_speed_mbs = models.IntegerField(default="")  # 寫入


class cartdb(models.Model):  # 購物清單資料表
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    user = models.CharField(max_length=255, default="")


class chassis(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址


class hdd(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    capacity_TB = models.FloatField(max_length=255, default="0.0")  # 容量
    size = models.CharField(max_length=255, default="")  # 尺寸
    Rotating_speed = models.CharField(max_length=255, default="")  # 轉速


class MB(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    foot_position_MB = models.CharField(max_length=255, default="")  # 名稱


class Memory(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    Memory_Specifications = models.CharField(
        max_length=255, default="")  # 記憶體類別
    capacity_GB = models.IntegerField(default="")  # 容量
    type = models.CharField(max_length=255, default="")  # 類型
    clock_rate = models.IntegerField(default="")  # 頻率


class Power(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=255, default="")
    url_list = models.CharField(max_length=255, default="")  # 商品連結
    pc_images = models.CharField(max_length=255, default="")  # 圖片網址
    Watts = models.CharField(max_length=255, default="")  # 名稱


class db(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=255, default="")  # 名稱
    name = models.CharField(max_length=255, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    url_list = models.CharField(max_length=3000, default="")  # 商品連結


class users(models.Model):
    account = models.CharField(max_length=255, null=False, default="")  # 帳號
    # 建立字串型別欄位，最大長度為255字元，預設值為空字串
    password = models.CharField(max_length=255, null=False, default="")  # 密碼
    email = models.EmailField(max_length=255, blank=False, default="")  # 信箱
    # 建立email型別欄位，最大長度為255字元，欄位不可空白，預設值為空字串
    username = models.CharField(max_length=255, default="")  # 姓名
    sex = models.BooleanField(null=False, default="")  # 性別
    linebotId = models.CharField(max_length=255, default="")  # 姓名


class prs(models.Model):
    account = models.CharField(max_length=255, null=False, default="")  # 帳號
    type = models.CharField(max_length=255, null=False, default="")
    time = models.CharField(max_length=255, null=False, default="")


class hit(models.Model):
    account = models.CharField(max_length=255, null=False, default="")  # 帳號
    cpu_hit = models.IntegerField(default=0)
    mb_hit = models.IntegerField(default=0)
    ssd_hit = models.IntegerField(default=0)
    hdd_hit = models.IntegerField(default=0)
    display_hit = models.IntegerField(default=0)
    memory_hit = models.IntegerField(default=0)
    power_hit = models.IntegerField(default=0)
    chassis_hit = models.IntegerField(default=0)


