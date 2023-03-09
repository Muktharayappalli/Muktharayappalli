from django.shortcuts import render,redirect
from apps.models import newdb,admindb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(req):
    return render(req,"index.html")


def newpage(req):
    return render(req,"addstudent.html")
def savedata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ag = request.POST.get('age')
        img = request.FILES['image']
        obj = newdb(name=na, age=ag, image=img)
        obj.save()
        return redirect(newpage)
def newhi(req):
    return render(req,"hi.html")

def displaypage(request):
    data = newdb.objects.all()
    return render(request,"displaystudent.html",{'data':data})

def newadmin(req):
    return render(req,"admin.html")
def newsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ba = request.POST.get('email')
        ca = request.POST.get('mob')
        da = request.POST.get('pas')
        ea = request.POST.get('passwd')
        fa = request.FILES['image']
        obj = admindb(name=na,email=ba,mob=ca,pas=da,passwd=ea,image=fa)
        obj.save()
        return redirect(newadmin)
def admindisplay(req):
    data = admindb.objects.all()
    return render(req,"admindisplay.html",{'data':data})

def editadminpage(req, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html",{'data':data})

def updateadmin(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ba = request.POST.get('email')
        ca = request.POST.get('mob')
        da = request.POST.get('pas')
        ea = request.POST.get('passwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(name=na,email=ba,mob=ca,pas=da,passwd=ea,image=file)
        return redirect(admindisplay)

def deleteadmin(req, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(admindisplay)

def logadmin(req):
    return render(req,"loginadmin.html")

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(index)
            else:
                return redirect(logadmin)
        else:
            return redirect(logadmin)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(logadmin)