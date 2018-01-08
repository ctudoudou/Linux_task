from django.db import models


# Create your models here.


class User(models.Model):
    """
    用戶表
    用戶名, 年齡, 密碼, 郵箱, 權限(1: 管理員 ,2: 工作人員 ,3: 用戶)
    """
    username = models.CharField(max_length=30, unique=True, null=False)
    age = models.IntegerField()
    password = models.CharField(max_length=64)
    email = models.EmailField()
    permission = models.IntegerField(default=3)


class Room(models.Model):
    """
    房屋表
    房屋編號, 價格, 房屋類別, 是否可用(1: 可用, 0:不可用), 是否租出(1: 未租出,2: 已出租,3: 已預訂), 預定/出租用戶
    """
    room_number = models.CharField(max_length=10, unique=True, null=False)
    price = models.IntegerField()
    img=models.ImageField(upload_to='./static/upload',default='img/l2.jpg')
    category = models.CharField(max_length=10)
    available = models.BooleanField(default=1)
    status=models.IntegerField(default=1)
    user=models.CharField(max_length=30,null=True)

