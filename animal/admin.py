from django.contrib import admin
from .models import User, Zhongzhu, Yangzhiziliao


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','user_gender','user_phone')
    search_fields = ['id','username']
    list_filter = ['user_gender']


class ZhongzhuAdmin(admin.ModelAdmin):
    list_display = ("biaohao", "zhushe", "pinzhong", "caishi", "tiwen", "xiwei", "jingye","yimiao","peizhong","zaizhu","houdai","creted_date", "user")
    search_fields = ['biaohao']

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(ZhongzhuAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Zhongzhu.objects.all()
        return Zhongzhu.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()



class YangzhiziliaoAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "creted_date")
    search_fields = ['title']

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(YangzhiziliaoAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Yangzhiziliao.objects.all()
        return Yangzhiziliao.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(User,UserAdmin)
admin.site.register(Zhongzhu, ZhongzhuAdmin)
admin.site.register(Yangzhiziliao, YangzhiziliaoAdmin)
