from django.db import models
from datetime import datetime
# Create your models here.

class Provinces(models.Model):
    name = models.CharField(max_length=50, verbose_name="省份")
    eng_name = models.CharField(max_length=50, verbose_name="省份英文", null=True)
    image = models.ImageField(upload_to="provinces/%Y/%m", verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    category = models.CharField(max_length=20, choices=(('hz', '华中'), ('hb', '华北'), ('hd', '华东'),
                                ('hn', '华南'), ('xb', '西北'), ('db', '东北'), ('xn', '西南')),
                                verbose_name='地区', default='hz')

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name