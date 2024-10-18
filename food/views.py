from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import itemform
from django.views.generic import CreateView
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    data=Item.objects.all()
    pro=request.GET.get('q')
    if pro  != "" and pro is not None:
        item=data.filter(item_name__icontains=pro)
    paginator=Paginator(data,4)
    page=request.GET.get('page')
    item=paginator.get_page(page)

    items={
        'item':item,
    }
    return render(request,'food/index.html',items)

def item(request):
    return HttpResponse("this is item page")

def details(request,item_id):
    data=Item.objects.get(pk=item_id)
    context={
        'item':data
    }
    return render(request,'food/detail.html',context)

def create_item(request):
    form=itemform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:idex')
    return render(request,'food/item_form.html',{'form':form})
# this is lass based view


class creatitem(CreateView):
        model=Item
        fields=['item_name','item_desc','image_price','item_image']
        template_name='food/item_form.html'


        def form_valid(self, form):
            form.instance.user_name=self.request.user
            return super().form_valid(form)
        

def update_item(request,item_id):
    item=Item.objects.get(id=item_id)
    form=itemform(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return render('food:idex')
    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item=Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('food:idex')
