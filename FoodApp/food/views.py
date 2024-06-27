# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# list view
from django.views.generic.list import ListView
# detail view
from django.views.generic.detail import DetailView
# create view, update view, delete view
from django.views.generic.edit import CreateView, UpdateView, DeleteView

'''
---------CLASS BASED VIEW---------
'''
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'image'] # fields that we want to display in the form
    template_name = 'food/item_form.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

class UpdateItem(UpdateView):
    model = Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'food/item_form.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
class DeleteItem(DeleteView):
    model = Item
    template_name = 'food/delete_item.html'
    success_url = '/index/'
    
    def get(self, request, *args, **kwargs):
        print("Get method called")
        return self.post(request, *args, **kwargs)
    

'''
---------FUNCTION BASED VIEW---------
'''
def index(request):
    # This function triggers when the user goes to the root URL.
    items = Item.objects.all() # make a list of all the items in the database
    template = loader.get_template('food/index.html')
    context = {
        'items': items,
    }
    # return HttpResponse(template.render(context,request)) # return the rendered template
    return render(request,'food/index.html',context) # return the rendered template using the render function

def detail(request, item_id):
    item = Item.objects.get(pk=item_id) # get the item with the primary key of item_id
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
    
def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        'form': form,
    }
    return render(request, 'food/item_form.html', context)

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'food/item_form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    context = {
        'item': item,
    }
    return render(request, 'food/delete_item.html', context)