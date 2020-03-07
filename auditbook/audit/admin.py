from django.contrib import admin
from .models import *


class StardandAdmin(admin.ModelAdmin):
    list_display = ['stdno','stdname','stdclass']


class ShouceAdmin(admin.ModelAdmin):
    list_display = ['shouceno','shoucename','shouceauthor','fileclass']


class PersonelAdmin(admin.ModelAdmin):
    list_display = ['name','position','profession']


class EquipAdmin(admin.ModelAdmin):
    list_display = ['equipname','equipno','equipmodel','equipfield']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['tabno','tabname','tabtype','tabtime']
    list_filter = ['tabtime']


admin.site.register(Stardands,StardandAdmin)
admin.site.register(Zhiliangshouce,ShouceAdmin)
admin.site.register(Personel,PersonelAdmin)
admin.site.register(Equip,EquipAdmin)
admin.site.register(Record,RecordAdmin)