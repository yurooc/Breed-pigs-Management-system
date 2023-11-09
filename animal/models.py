from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import  AbstractUser
# from ckeditor.fields import RichTextField, RichTextUploadingField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
# 站点信息表
class Site_Info(models.Model):
    icon = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)

# 用户表
class User(AbstractUser):

    class Meta:
    # 定义在管理后台显示的名称
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
           
    # 用户名,由于继承了自带的User对象,所以多余了,注释掉
    #user_name = models.CharField(max_length=10,verbose_name='用户名')
    
    # 用户性别 布尔值，True为男
    gender_choice = (
        ('男','男'),
        ('女','女')
    )
    user_gender = models.CharField(max_length=10,choices=gender_choice,verbose_name='性别')
    
    # 用户的电话号码
    user_phone = models.CharField(max_length=11,verbose_name='联系电话')
    
    # 用户的头像

    # 密码,由于继承了自带的User对象,所以多余了,注释掉
    #user_pwd = models.CharField(max_length=255,verbose_name='用户密码')

    def __str__(self):
        return self.username

class Zhongzhu(models.Model):
    pinzhong_choice = (
        ('种公猪', '种公猪'),
        ('种母猪', '种母猪'),
    )
    caishi_choice = (
        ('优', '优'),
        ('良好', '良好'),
        ('异常', '异常'),
    )
    xiwei_choice = (
        ('无异常', '无异常'),
        ('跛足', '跛足'),
        ('惊厥', '惊厥'),
        ('攻击', '攻击'),
        ('爬跨', '爬跨'),
    )
    jingye_choice = (
        ('优', '优'),
        ('良', '良'),
        ('异常', '异常'),
        ('无', '无'),
    )
    yimiao_choice = (
        ('是', '是'),
        ('否', '否'),
    )
    peizhong_choice = (
        ('是', '是'),
        ('否', '否'),
    )
    zaizhu_choice = (
        ('是', '是'),
        ('否', '否'),
    )
    # 编号， 猪舍， 品种， 采食， 体温， 行为， 精液质量， 添加者， 添加时间
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="管理员", related_name='entries', editable=False)
    biaohao = models.IntegerField(verbose_name="编号", default=0)
    zhushe = models.IntegerField(verbose_name="猪舍", default=1)
    pinzhong = models.CharField(max_length=255, verbose_name="品种",choices=pinzhong_choice)
    caishi = models.CharField(max_length=255, verbose_name="采食",choices=caishi_choice)
    tiwen = models.CharField(max_length=11, verbose_name="体温")
    xiwei = models.CharField(max_length=255, verbose_name="行为",choices=xiwei_choice)
    jingye = models.CharField(max_length=255, verbose_name="精液质量",choices=jingye_choice)
    creted_date = models.DateTimeField(verbose_name="记录提交时间", default=datetime.datetime.now, editable=False)
    yimiao = models.CharField(max_length=255,verbose_name="是否疫苗免疫",choices=yimiao_choice)
    peizhong = models.CharField(max_length=255,verbose_name="是否已经配种",choices=peizhong_choice)
    zaizhu = models.CharField(max_length=255,verbose_name="是否为仔猪",choices=zaizhu_choice)
    houdai = models.CharField(max_length=255,verbose_name="后代种猪编号")

    def save(self, *args, **kwargs):
        self.usuario = User
        super(Zhongzhu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "种猪信息"
        verbose_name_plural = "种猪信息"


class Yangzhiziliao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="管理员", related_name='entries1', editable=False)
    title = models.CharField(max_length=32, verbose_name="标题")
    # neirong = models.RichTextField(verbose_name="内容")
    neirong = RichTextUploadingField('文章内容',default='文章内容')
    creted_date = models.DateTimeField(verbose_name="记录提交时间", default=datetime.datetime.now, editable=False)

    def short_detail(self):
        if len(str(self.neirong)) > 30:
            return '{}...'.format(str(self.neirong)[0:29])
        else:
            return str(self.neirong)
    short_detail.allow_tags = True
    short_detail.short_description = u'文章内容'
    def save(self, *args, **kwargs):
        self.usuario = User
        super(Yangzhiziliao, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "养猪知识"
        verbose_name_plural = "养猪知识"

class Siliao(models.Model):
        sname = models.CharField(max_length=255,verbose_name="饲料名称")
        kucun = models.CharField(max_length=255,verbose_name="库存")



class Peizhong(models.Model):
        bianhao = models.IntegerField(verbose_name="编号", default=0)
        jiluneirong = models.CharField(max_length=255,verbose_name="记录内容")
class Renjian(models.Model):
        bianhao = models.IntegerField(verbose_name="编号", default=0)
        jiluneirong = models.CharField(max_length=255, verbose_name="记录内容")
class Fenmian(models.Model):
        bianhao = models.IntegerField(verbose_name="编号", default=0)
        jiluneirong = models.CharField(max_length=255, verbose_name="记录内容")
class Caijing(models.Model):
        bianhao = models.IntegerField(verbose_name="编号", default=0)
        jiluneirong = models.CharField(max_length=255, verbose_name="记录内容")
class Xingweiy(models.Model):
        bianhao = models.IntegerField(verbose_name="编号", default=0)
        jiluneirong = models.CharField(max_length=255, verbose_name="记录内容")