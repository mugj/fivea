import xadmin

from .models import Scenerys

class ScenerysAdmin():
    pass

xadmin.site.register(Scenerys, ScenerysAdmin)