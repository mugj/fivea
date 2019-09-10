from django.shortcuts import render
from provinces.models import Provinces
from django.views.generic import View
from guide.models import Guide

# Create your views here.
# def provincesList(request):
#     provinces_list = Provinces.objects.all()
#     return render(request, "gallery.html", {
#         'provinces_list': provinces_list,
#     })
#
#
# def indexData(request):
#     provinces_list = Provinces.objects.all()
#     return render(request, "index.html", {
#         'provinces_list': provinces_list,
#     })
class ProvincesListView(View):
    def get(self, request):
        provinces_list = Provinces.objects.all()
        return render(request, "gallery.html", {
            'provinces_list': provinces_list,
        })

class IndexDataView(View):
    def get(self, request):
        provinces_list = Provinces.objects.all()
        guide_list = Guide.objects.filter(is_index=True)
        return render(request, "index.html", {
            'provinces_list': provinces_list,
            'guide_list': guide_list,

        })
