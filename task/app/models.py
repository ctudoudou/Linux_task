from django.db import models


# Create your models here.


class User(models.Model):
    """
    用戶表
    用戶名, 年齡, 密碼, 郵箱, 權限(1: 管理員 ,2: 工作人員 ,3: 用戶)
    """
    username = models.CharField(max_length=30, unique=True, null=False)
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    permission = models.IntegerField(default=3)


class Room(models.Model):
    """
    房屋表
    房屋編號, 價格, 圖片，房屋類別, 是否可用(1: 可用, 0:不可用), 是否租出(1: 未租出,2: 已出租,3: 已預訂), 預定/出租用戶, 評價, 預定次數, 評價分數
    """
    room_number = models.CharField(max_length=10, unique=True, null=False)
    price = models.IntegerField()
    img = models.ImageField(upload_to='./static/upload/', default='img/l2.jpg')
    category = models.CharField(max_length=10)
    available = models.BooleanField(default=1)
    status = models.IntegerField(default=1)
    user = models.CharField(max_length=30, null=True)
    evaluation = models.CharField(max_length=100, default='暫無評價')
    number = models.IntegerField(default=0)
    fraction = models.CharField(max_length=10, default='star2.png')


class Latest_post(models.Model):
    """
    帖子
    標題, 發布時間, 發布人, 內容, 配圖, 浏览次数
    """
    title = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    img = models.ImageField(upload_to='./static/upload/')
    views = models.IntegerField(default=1)


class Subscription(models.Model):
    """
    訂閱用戶
    郵箱地址(無效驗), 訂閱時間
    """
    email=models.EmailField()
    time=models.DateTimeField(auto_now_add=True)