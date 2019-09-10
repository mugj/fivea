from django.db import models
from datetime import datetime
from scenerys.models import Scenerys
# Create your models here.
class Guide(models.Model):
    guide_sce = models.ForeignKey(Scenerys, verbose_name='景区攻略', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="标题")
    detail = models.TextField(verbose_name="详情")
    image = models.ImageField(upload_to="scenerys/%Y/%m", verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    is_index = models.BooleanField(default=False, verbose_name="是否首页")

    class Meta:
        verbose_name = "攻略"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
