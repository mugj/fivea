import xadmin

from .models import Guide

class GuideAdmin():
    pass

xadmin.site.register(Guide, GuideAdmin)