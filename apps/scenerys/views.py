from django.shortcuts import render
from scenerys.models import Scenerys
from provinces.models import Provinces
from django.views.generic import View


class SceneryListView(View):
    def get(self, request, provinces_id):
        if int(provinces_id) == 0:
            scenery_list = Scenerys.objects.all()
            return render(request, "scenery.html", {
                'scenery_list': scenery_list,
            })
        else:
            provinces_sce = Provinces.objects.get(id=int(provinces_id))
            scenery_list = provinces_sce.scenerys_set.all()
            return render(request, "scenery.html", {
                'scenery_list': scenery_list,
            })



class SceneryView(View):
    def get(self, request, scenery_id):
        scenery = Scenerys.objects.get(id=int(scenery_id))
        return render(request, "single.html", {
            'scenery': scenery,
        })