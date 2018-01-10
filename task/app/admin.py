from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Room)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'category', 'price', 'available', 'status', 'user')
    list_display_links = ('room_number', 'available', 'status')
    list_filter = ('category', 'available', 'status')


@admin.register(Subscription)
class Subscription_(admin.ModelAdmin):
    list_display = ('id', 'email', 'time')


@admin.register(Latest_post)
class Subscription_(admin.ModelAdmin):
    list_display = ('id', 'title', 'time', 'author', 'content', 'img', 'views')


@admin.register(Hotel_environment)
class Subscription_(admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'content')
    readonly_fields = ('image_tag',)
    # (optional)若無此行，則會多出一個欄位顯示 image 的 url 與上傳圖片按鈕，如果希望從後台可以修改圖片，可將此行刪除
    exclude = ('image_file',)


admin.site.site_header = '酒店管理系統'
admin.site.site_title = '房屋管理'
