from django.shortcuts import render

# Create your views here.
# in views.py
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Module

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView

# class Home(View):
#     def get(self, request):
#         return HttpResponse("New England Synth Home")

class ManufacturerList(TemplateView):
    template_name = "maufacturer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manufacturers"] = ManufacturerList.objects.all()
        return context

class ManufacturerCreate(CreateView):
    model = Manufacturerfields = ['name','img','info','function']
    template_name = "manufacturer_create.html"
    success_url = "/modules/"