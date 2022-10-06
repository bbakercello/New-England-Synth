# at top of file
from email.mime import image
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Manufacturer, Module, Store
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

    # adding store context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

# @method_decorator(login_required, name='dispatch')
class ManufacturerList(TemplateView):
    template_name = "manufacturer_list.html"
#     In here, I want to check if there has been a query made
# I know the queries will have a key of name
# const context = {
#     manufacturers: //finding manufacturerList,
#     stuff_at_top: "This is a string"
# }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mySearchName = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if mySearchName != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["manufacturers"] = Manufacturer.objects.filter(name__icontains=mySearchName)
            context["stuff_at_top"] = f"Searching through Manufacturers list for {mySearchName}"
        else:
            # context["manufacturers"] = Manufacturer.objects.filter(user=self.request.user)
            context["stuff_at_top"] = "Trending Manufacturers"
        return context

# @method_decorator(login_required, name='dispatch')
class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = ['name', 'img']
    template_name = "manufacturer_create.html"

    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        # form.instance = {
            # name: Baby Shark 2,
            # img: my image url,
        # }
        # form.instance.user = self.request.user
        # form.instance = {
            # name: Another Test,
            # img: a.com,
            # user: self.request.user
        # }
       
        return super(ManufacturerCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('manufacturer_detail', kwargs={'pk': self.object.pk})

# @method_decorator(login_required, name='dispatch')
class ManufacturerDetail(DetailView):
    model = Manufacturer
    template_name = "manufacturer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        context ['modules'] = Module.objects.all()
        return context

# @method_decorator(login_required, name='dispatch')
class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = ['name', 'img']
    template_name = "manufacturer_update.html"
    success_url = "/manufacturers/"

    def get_success_url(self):
        return reverse('manufacturer_detail', kwargs={'pk': self.object.pk})

# @method_decorator(login_required, name='dispatch')
class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = "manufacturer_delete_confirmation.html"
    success_url = "/manufacturers/"

# @method_decorator(login_required, name='dispatch')
class ModuleCreate(View):

    def post(self, request, pk):
        formTitle = request.POST.get("name")
        img = request.POST.get("img")
        info = request.POST.get("info")
        function = request.POST.get("function")
        theManufacturer = Manufacturer.objects.get(pk=pk)
        Module.objects.create(name=formTitle, img = img,info = info, function = function, manufacturer=theManufacturer)
        return redirect('manufacturer_detail', pk=pk)

class StoreModuleAssoc(View):

    def get(self, request, pk, module_pk):
        # get the query parameter from the 
        assoc = request.GET.get("assoc")

        if assoc == "remove":
            # get the store by the pk, remove the module (row) with the module_pk
            Store.objects.get(pk=pk).modules.remove(module_pk)
        
        if assoc == "add":

            # get the store by the pk, add the module (row) with the module_pk
            Store.objects.get(pk=pk).modules.add(module_pk)
        
        return redirect('home')

# class Signup(View):
#     # show a form to fill out
#     def get(self, request):
#         form = CreationForm()
#         context = {"form": form}
#         return render(request, "registration/signup.html", context)
#     # on form submit, validate the form and login the user.
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("manufacturer_list")
#         else:
#             return redirect("si