from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Database,Detials

# Create your views here.
def home(request):
	return render(request,'home.html')

def save(request):
	obj=Database(
		fname=request.POST.get("fname"),
		lname=request.POST.get("lname"),
		phoneno=request.POST.get("phoneno"))
	obj.save()
	obj.save(using='login')
	return render(request,'save.html',{'obj':obj})

def home1(request):
	return render(request,'home1.html')


def save1(request):
	obj=Detials(
		username=request.POST.get("username"),
		password=request.POST.get("password"),
		phoneno=request.POST.get("phoneno"))
	obj.save(using='login12')
	return HttpResponse("sucess")