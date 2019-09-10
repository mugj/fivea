from django.db import models
from datetime import datetime
from provinces.models import Provinces
# Create your models here.
class Scenerys(models.Model):
    scen_prov = models.ForeignKey(Provinces, verbose_name='景区省份', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="景区名称")
    desc = models.CharField(max_length=300, verbose_name="简介")
    detail = models.TextField(verbose_name="详情")
    image = models.ImageField(upload_to="scenerys/%Y/%m", verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "景区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
