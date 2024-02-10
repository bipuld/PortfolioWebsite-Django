from django.shortcuts import render,redirect,HttpResponse
from . models import Contact,About,Skill,SkillChoice,Counter,CounterSection,Service
from .models import EduDetail
from .models import Summary_sec
from .models import ProfessionalWork,Pro_detail
from django.template.loader import get_template
import os
from xhtml2pdf import pisa
from django.contrib import messages
# Create your views here.
def home(request):
    skill=SkillChoice.objects.all()
    counter=Counter.objects.all()
    summary=Summary_sec.objects.get(id=1)
    eduation=EduDetail.objects.all()
    profession=Pro_detail.objects.all()
    context={
        'skills':skill,
        'counts':counter,
        'summary':summary,
        'education':eduation,
        'profession':profession,
    }
    return render(request,'main/home.html',context)

def about(request):
    details=About.objects.get(id=1)
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
    details=About.objects.get(id=1)
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



# resumee modifaction
def resumee(request):
    summary=Summary_sec.objects.get(id=1)
    eduation=EduDetail.objects.all()
    profession=Pro_detail.objects.all()
    context={
        'summary':summary,
        'education':eduation,
        'profession':profession
    }
    return render(request,'main/resumee.html',context)

def service_detail(request,id):
    service_details=Service.objects.get(id=id)
    context={
        'service_detail':service_details
    }
    return render(request,'main/service_details.html',context)



# resume download pdf

def resume_pdf(request):
    summary=Summary_sec.objects.get(id=1)
    eduation=EduDetail.objects.all()
    profession=Pro_detail.objects.all()
    
    # downloads file 
    template=get_template('main/resume_generate_pdf')
    context=({
        'summary':summary,
        'education':eduation,
        'profession':profession
        
    })
    # create pdf response 
    html=template.render(context)
    print(html)

    # Prepare the HTTP response with PDF content
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']="filename=Bipul_resume.pdf"
    
    
    pdf=pisa.CreatePDF( html.encode('utf-8'),
        dest=response,)
    
    
    if not pdf.err:
        return response

    return HttpResponse('Error generating PDF: {}'.format(pdf.err), content_type='text/plain')