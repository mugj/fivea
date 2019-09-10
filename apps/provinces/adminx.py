import xadmin

from .models import Provinces

class ProvincesAdmin():
    pass

xadmin.site.register(Provinces, ProvincesAdmin)