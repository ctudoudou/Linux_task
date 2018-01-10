from django.db import models
from django.utils.html import format_html

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
    room_number = models.CharField(max_length=10, unique=True, null=False,verbose_name='房屋編號')
    price = models.IntegerField(verbose_name='價格')
    img = models.ImageField(upload_to='./static/upload/', default='img/l2.jpg',verbose_name='圖片')
    category = models.CharField(max_length=10,verbose_name='房屋類別')
    available = models.BooleanField(default=1,verbose_name='是否可用')
    status = models.IntegerField(default=1,verbose_name='是否租出')
    user = models.CharField(max_length=30, null=True,verbose_name='預定/出租用戶')
    evaluation = models.CharField(max_length=100, default='暫無評價',verbose_name='評價')
    number = models.IntegerField(default=0,verbose_name='預定次數')
    fraction = models.CharField(max_length=10, default='star2.png',verbose_name='評價分數')

    def status_(self):
        if self.status==1:
            return format_html(
                '<span style="color: #{green};">{}</span>',
                '未出租',
            )
        else:
            return format_html(
                '<span style="color: #{red};">{}</span>',
                '已出租',
            )


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
    email=models.EmailField(verbose_name='郵箱')
    time=models.DateTimeField(auto_now_add=True,verbose_name='時間')

    def __str__(self):
        return '訂閱用戶'


class Hotel_environment(models.Model):
    """
    酒店環境數據庫
    圖片名稱, 圖片文件, 圖片簡介
    """
    title=models.CharField(max_length=10)
    img=models.ImageField(upload_to='./static/upload/')
    content=models.CharField(max_length=100)

    def image_tag(self):
        return u'<img src="/%s" width="200px" />' % self.img.url


