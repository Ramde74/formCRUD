from django.shortcuts import render, redirect
from .models import *
from.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def booklist(request):
    book = Book.objects.all()
    return render(request, 'listbook.html',{'book':book})

def addbook(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('booklist')

    return render(request, 'addbook.html', {'form':form})

def deletebook(request,id):
    s = Book.objects.get(id=id)
    s.delete()
    book = Book.objects.all()
    return render(request, 'listbook.html', {'book': book})

def updatebook(request,id):
    s = Book.objects.get(id=id)
    form = BookForm(request.POST or None,instance=s)

    if form.is_valid():
        form.save()
        return redirect('booklist')

    return render(request, 'updatebook.html', {'form': form,'s':s})


