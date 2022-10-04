from django.shortcuts import redirect
from django.views import View
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Manufacturer,Module
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
#         return HttpResponse("New England Synth Home")

class ManufacturerList(TemplateView):
    template_name = "manufacturer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mySearchName = self.request.GET.get("name")

        if mySearchName != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["manufacturers"] = Manufacturer.objects.filter(name__icontains=mySearchName)
            context["stuff_at_top"] = f"Searching through Manufacturers list for {mySearchName}"
        else:
            context["manufacturers"] = Manufacturer.objects.all()
            context["stuff_at_top"] = "Trending Manufacturers"
        return context

class ManufacturerCreate(CreateView):
    model = Manufacturerfields = ['name','img','info','function']
    template_name = "manufacturer_create.html"
    success_url = "/manufacturers/"

class ManufacturerDetail(DetailView):
    model = Manufacturer
    template_name = "manufacturer_detail.html"

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = ['name', 'img', 'bio', 'verified_manufacturer']
    template_name = "manufacturer_update.html"
    success_url = "/manufacturers/"

    def get_success_url(self):
        return reverse('manufacturer_detail', kwargs={'pk': self.object.pk})

class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = "Manufacturer_delete_confirmation.html"
    success_url = "/Manufacturers/"

class ModuleCreate(View):

    def post(self, request, pk):
        formTitle = request.POST.get("name")
        img = request.POST.get("img")
        info = request.POST.get("info")
        function = request.POST.get("function")
        theManufacturer = Manufacturer.objects.get(pk=pk)
        Module.objects.create(name=formTitle, img=img,info=info, function=function, manufacturer=theManufacturer)
        return redirect('manufacturer_detail', pk=pk)