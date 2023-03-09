from django.shortcuts import render,redirect
from backend.models import regdb

# Create your views here.

def homepage(req):
    data = newdb.objects.all()
    da = admindb.objects.all()
    return render(req,"home.html",{'data':data, 'da':da})
    # return render(req,"home.html")
def about(req):
    return render(req,"aboutus.html")
def productdis(req, itemCatg):
    print("===itemCatg===",itemCatg)
    catg = itemCatg.upper()
    products = admindb.objects.filter(Category=itemCatg)
    context = {
        'products':products,
        'catg': catg
    }
    return render(req,"productdisplay.html",context)

def singledis(req):
    return render(req,"singleprdt.html")

def regipage(req):
    return render(req,"regpage.html")
def loginpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ba = request.POST.get('email')
        ca = request.POST.get('mob')
        da = request.POST.get('pas')
        ea = request.POST.get('passwd')
        obj = regdb(name=na,email=ba,mob=ca,pas=da,passwd=ea)
        obj.save()
        return redirect(regipage)

def contactpg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ba = request.POST.get('email')
        ca = request.POST.get('subject')
        da = request.POST.get('message')
        obj = contactdb(name=na,email=ba,subject=ca,message=da)
        obj.save()
        return redirect(contactpg)