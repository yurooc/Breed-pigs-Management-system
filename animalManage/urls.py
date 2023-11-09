"""animalManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    url(r'', include('ckeditor_uploader.urls')),
    path('xinxiyulan/', views.xinxiyulan),
    path('xiputu/', views.xiputu),
    path('shengchantishi/', views.shengchantishi),
    path('siliaokucun/', views.siliaokucun),
    path('xingweijilu/', views.xingweijilu),
    path('siliaoadd/',views.siliaoadd),
    path('sdelete/', views.sdelete),
    path('edit/<int:nid>/', views.edit),
    path('chartbar/',views.chart_bar),
    path('chartbing/',views.chart_bing),
    path('chartzong/',views.chart_zong),
    path('chartku/',views.chart_ku),
    path('chartgraph/',views.chart_graph),
    path('peiadd/',views.peiadd),
    path('peidelete/',views.peidelete),
    path('renadd/',views.renadd),
    path('rendelete/',views.rendelete),
    path('fenadd/',views.fenadd),
    path('fendelete/',views.fendelete),
    path('caiadd/',views.caiadd),
    path('caidelete/',views.caidelete),
    path('yadd/',views.yadd),
    path('ydelete/',views.ydelete),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
