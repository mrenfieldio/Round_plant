from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context={}
    db=package.objects.all()
    context["db"]=db
    cb=testimonials.objects.all()
    context["cb"]=cb
    nb=events.objects.all()
    context["nb"]=nb
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')

          if request.POST:
              messages.success(request,'sucessfully updated')
              details=contact_detail.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
              details.save()
              return redirect('index')
    return render(request,'index.html',context)



def base(request,p):
     # b=package.objects.get(pk=p)
     m=sub_packages.objects.filter(pack=p)
     return render(request,'base.html',{"m":m})  

def about(request):
     
     return render(request,'about.html')   
    
def packages(request):
     o=package.objects.all()
     return render(request,'packages.html',{'db':o})

def events1(request) :
      m=events.objects.all()
      return render(request,'events.html',{'db':m})

def gallery(request) :
     m=package.objects.all()
     return render(request,'gallery.html',{'db':m})

def contact(request) :
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')

          if request.POST:
               messages.success(request,'sucessfully updated')
               details=contact_detail.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
               details.save()
               return redirect('contact')
          
           
     return render(request,'contact.html')

def gallery(request) :
     m=package.objects.all()
     return render(request,'gallery.html',{'db':m})

def eventsin(request,p) :
     n=events.objects.get(pk=p)
     return render(request,'events_in.html',{'db':n})

def package1(request,p):
     # n=package.objects.get(pk=p)
     # nb=n.cleaned_data['place']
     m=sub_packages.objects.get(pk=p)
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')
          if request.POST:
               messages.success(request,'sucessfully updated')
               details=contact_detail.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
               details.save()
               return index(request)      
     return render(request,'package1.html',{'db':m})
    