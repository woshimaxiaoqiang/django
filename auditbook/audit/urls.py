from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('reg',views.reg,name='reg'),
    path('logout',views.logout,name='logout'),
    path('report',views.zhunze,name='report'),
    path('tixi',views.tixi,name='tixi'),
    path('jilus',views.jilus,name='jilus'),
    path('jilu/<tab_time>',views.jilu,name='jilu'),
    path('record',views.record,name='record'),
    path('getready',views.getready,name='getready'),
    path('uploadfile',views.uploadfile,name='uploadfile'),
    path('uploadstd',views.uploadstd,name='uploadstd'),
    path('uploadrecord',views.uploadrecord,name='uploadrecord'),
    path('addperson',views.addperson,name='addperson'),
    path('addequip',views.addequip,name='addequip'),
    path('deleteshouce/<slug:shouceid>',views.deleteshouce,name='deleteshouce'),
    path('deletestd/<slug:stdid>',views.deletestd,name='deletestd'),
    path('deleteper/<slug:perid>',views.deleteper,name='deleteper'),
    path('records/<tab_time>',views.records,name='records'),
    path('test_ajax/',views.test_ajax,name='ajax'),
    path('yanzhm',views.yanzhm,name='yanzhm'),
    # path('valid_code',views.valid_code,name='valid_code'),
    path('cms',views.cms,name='cms'),
]
