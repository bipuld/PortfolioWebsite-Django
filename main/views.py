from django.shortcuts import render,redirect
from . models import Contact,About,Skill,SkillChoice,Counter,CounterSection,Service
from django.contrib import messages
# Create your views here.
def home(request):
    skill=SkillChoice.objects.all()
    counter=Counter.objects.all()
    context={
        'skills':skill,
        'counts':counter
    }
    return render(request,'main/home.html',context)

def about(request):
    details=About.objects.get(id=2)
    context={
        'detail':details
    }
    return render(request,'main/about.html',context)

def facts(request):
    return render(request,'main/facts.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact_form=Contact(name=name,email=email,subject=subject,message=message)
        contact_form.save()
        print(request.POST)
        messages.success(request,'Your message has been sent successfully.')
        return redirect('contact')
    else:
        contact_form=Contact.objects.all()
    details=About.objects.get(id=2)
    context={
        'detail':details
    }
    return render(request,'main/contact.html',context)

def portfolio(request):
    return render(request,'main/portfolio.html')

def service(request):
    service=Service.objects.all().order_by('id')
    context={
        'services':service

    }
    return render(request,'main/service.html',context)
def skills(request):
    return render(request,'main/skills.html')

def resumee(request):
    return render(request,'main/resumee.html')

def service_detail(request,id):
    service_details=Service.objects.get(id=id)
    context={
        'service_detail':service_details
    }
    return render(request,'main/service_details.html',context)