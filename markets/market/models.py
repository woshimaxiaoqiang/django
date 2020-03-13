from django.db import models


class SaleList(models.Model):
    productno = models.CharField('商品序列码',max_length=100)

    class Meta:
        verbose_name_plural = '销售清单'
    def __str__(self):
        return 'SaleList:{}'.format(self.productno)





