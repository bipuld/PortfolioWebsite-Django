from django.urls import path,include
from . import views
# from main.views import GeneratePDF
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('facts/',views.facts,name='facts'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('service/',views.service,name='service'),
    path('skills/',views.skills,name='skills'),
    path('resumee/',views.resumee,name='resumee'),
    path('resume_pdf/',views.resume_pdf,name='resume_pdf'),
    path('service_detail/<int:id>/',views.service_detail,name='service_detail'),
    # path('generate-pdf/', GeneratePDF.as_view(), name='generate_pdf'),
]