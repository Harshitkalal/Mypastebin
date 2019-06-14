from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from .models import Paste
from django.utils import timezone


def home(request):
    return render(request,'paste/home.html')

def create(request):
    paste = Paste()
    paste.text = request.POST['text']
    paste.name = request.POST['name']
    paste.created_on = timezone.datetime.now()
    paste.updated_on = timezone.datetime.now()
    paste.save()
    return render(request,'paste/home.html')

def update(request,id):

    paste=Paste()
    paste=Paste.objects.get(pk=id)
    paste.text=request.POST.get('text')
    paste.name=request.POST.get('name')
    paste.updated_on=timezone.datetime.now()
    paste.save()
    return render(request,'paste/home.html')


def edit(request,id):
    paste =Paste.objects.get(pk=id)
    return render(request,'paste/update.html',{'paste':paste})



#def delete(request,id):


def detail(request,id):
    paste= get_object_or_404(Paste,pk=id)
    return render(request,'paste/detail.html',{'paste':paste})

def allpaste(request):
    allpaste = Paste.objects
    return render(request,'paste/allpaste.html',{'allpaste':allpaste})


def pastedelete(request,id):
    paste=Paste.objects.get(pk=id)
    paste.delete()
    return redirect('/allpaste')

#class PasteDetail(DetailView):
 #   model = Paste
  #  template_name = "pastebin/paste_detail.html"
