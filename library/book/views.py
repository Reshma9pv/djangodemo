from django.shortcuts import render
from book.models import Book
from book.forms import BookForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p= request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,image=i)
        b.save()
        return view(request)
    return render(request,'add.html')

# def add(request):
#     if(request.method=="POST"):
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return view(request)
#     form=BookForm()
#     return render(request,'add1.html',{'form':form})
@login_required
def view(request):
    b=Book.objects.all()
    return render(request,'view.html',{'book':b})
@login_required
def viewbook(request,p):
    b=Book.objects.get(id=p)
    return render(request,'viewbook.html',{'b':b})
@login_required
def deletebook(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return view(request)

@login_required
def editbook(request,p):
    b=Book.objects.get(id=p)
    if(request.method == "POST"):
      form=BookForm(request.POST,request.FILES,instance=b)
      if form.is_valid():
         form.save()
         return view(request)

    form=BookForm(instance=b)

    return render(request,'edit.html',{'f':form})
