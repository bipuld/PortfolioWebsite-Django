from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Contact, About, Skill, SkillChoice, Counter, EduDetail, Summary_sec, ProfessionalWork, Pro_detail, Service
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from django.http import Http404
# Home view
def home(request):
    skills = SkillChoice.objects.all()
    counters = Counter.objects.all()
    try:
        summary = Summary_sec.objects.get(id=1)
    except Summary_sec.DoesNotExist:
        summary = None
    education = EduDetail.objects.all()
    profession = Pro_detail.objects.all()
    
    context = {
        'skills': skills,
        'counts': counters,
        'summary': summary,
        'education': education,
        'profession': profession,
    }
    return render(request, 'main/home.html', context)

# About view
def about(request):
    try:
        details = get_object_or_404(About, id=1)
    except Http404:
        details = None
        
    context = {'detail': details}
    return render(request, 'main/about.html', context)

# Facts view
def facts(request):
    return render(request, 'main/facts.html')

# Contact view
def contact(request):
    print("Hello")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact_form = Contact(name=name, email=email, subject=subject, message=message)
        contact_form.save()
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')


    try:
        details = get_object_or_404(About, id=1)
    except Http404:
        details = None
    context = {'detail': details}
    return render(request, 'main/contact.html', context)

# Portfolio view
def portfolio(request):
    return render(request, 'main/portfolio.html')

# Service view
def service(request):
    services = Service.objects.all().order_by('id')
    context = {'services': services}
    return render(request, 'main/service.html', context)

# Skills view
def skills(request):
    return render(request, 'main/skills.html')

# Resumee view
def resumee(request):
    try:
        summary = get_object_or_404(Summary_sec, id=1)
    except Http404:
        summary = None
    education = EduDetail.objects.all()
    profession = Pro_detail.objects.all()
    
    context = {
        'summary': summary,
        'education': education,
        'profession': profession
    }
    return render(request, 'main/resumee.html', context)

# Service detail view
def service_detail(request, id):
    try:
        service_detail = get_object_or_404(Service, id=id)
    except Http404:
        service_detail = None
    context = {'service_detail': service_detail}
    return render(request, 'main/service_details.html', context)

# Resume PDF download view
def resume_pdf(request):
    try:
        summary = get_object_or_404(Summary_sec, id=1)
    except Http404:
        summary = None
    education = EduDetail.objects.all()
    profession = Pro_detail.objects.all()
    
    template = get_template('main/resume_generate_pdf.html')
    context = {
        'summary': summary,
        'education': education,
        'profession': profession
    }
    html = template.render(context)

    # Prepare the HTTP response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Bipul_resume.pdf"'
    
    pdf = pisa.CreatePDF(html.encode('utf-8'), dest=response)
    
    if not pdf.err:
        return response

    return HttpResponse(f'Error generating PDF: {pdf.err}', content_type='text/plain')


