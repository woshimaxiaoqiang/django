from django.db import models
from django.contrib.auth.models import User

class Zhiliangshouce(models.Model):
    authorlist = [(v['username'],v['username']) for i, v in enumerate(User.objects.values('username'))]
    fileclasses = [('质量手册','质量手册'),('程序文件','程序文件'),('三层次文件','三层次文件'),('技术管理规定','技术管理规定'),
                   ]
    shouceno = models.CharField('文件编号',max_length=20)
    shoucename = models.CharField('文件名称',max_length=100)
    shouceauthor = models.CharField('编制者',max_length=20,choices=authorlist)
    shouceadd = models.FileField('选择地址',upload_to='../media/shouce/',default='')
    fileclass = models.CharField('文件分类',choices=fileclasses,max_length=20)
    class Meta:
        verbose_name_plural='体系文件'
    def __str__(self):
        return 'Zhiliangshouce:{}{}{}'.format(self.shouceno,self.shoucename,self.shouceauthor)


class Stardands(models.Model):
    stdlist = [('AC','AC'),('CNAS/DILAC','CNAS/DILAC'),('ASTM','ASTM'),('GB','GB')]
    stdno = models.CharField('文件编号',max_length=20)
    stdname = models.CharField('文件名称',max_length=50)
    stdadd = models.FileField('选择地址',upload_to='../media/standard/',default='')
    stdclass = models.CharField('文件分类',choices=stdlist,max_length=20)
    class Meta:
        verbose_name_plural='准则/标准'
    def __str__(self):
        return 'Stardands:{}{}{}'.format(self.stdno,self.stdname,self.stdclass)


class Personel(models.Model):
    profession_list = [('实验室主任','实验室主任'),('质量负责人','质量负责人'),
                       ('技术负责人','技术负责人'),('QA人员','QA人员'),
                       ('授权签字人','授权签字人'),('内审员','内审员'),
                       ('化学技术人员','化学技术人员'),('机性技术人员','机性技术人员'),
                       ('金相技术人员','金相技术人员')]
    name = models.CharField('姓名',max_length=20)
    position = models.CharField('职位',max_length=20)
    profession = models.CharField('专业',max_length=20,choices=profession_list)
    class Meta:
        verbose_name_plural='人员'
    def __str__(self):
        return 'Personel:{}{}{}'.format(self.name,self.position,self.profession)


class Equip(models.Model):
    equipfield_list = [('化学','化学'),('机性','机性'),('金相','金相'),
                       ('计量器具','计量器具'),('其他设备','其他设备')]
    equipname = models.CharField('设备名称',max_length=50)
    equipno = models.CharField('设备编号',max_length=50)
    equipmodel = models.CharField('设备型号',max_length=50)
    equipfield = models.CharField('所属专业',max_length=20,choices=equipfield_list)
    class Meta:
        verbose_name_plural='设备'
    def __str__(self):
        return 'Equip:{}{}{}{}'.format(self.equipname,self.equipname,self.equipmodel,self.equipfield)


class Record(models.Model):
    tablist = [('质量记录','质量记录'),('技术记录','技术记录'),
               ('内审记录','内审记录'),('NCR记录','NCR记录')]
    tabno = models.CharField('记录编号',max_length=20)
    tabname = models.CharField('记录名称',max_length=30)
    tabtype = models.CharField('记录类型',max_length=20,choices=tablist)
    tabfile = models.FileField('上传记录',upload_to='../media/records/',default='')
    tabtime = models.DateField('记录时间')
    class Meta:
        verbose_name_plural='历年记录'
    def __str__(self):
        return 'Record:{}{}{}{}'.format(self.tabno,self.tabname,self.tabtype,self.tabtime)
