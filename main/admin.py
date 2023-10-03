from django.contrib import admin
from django.utils.html import format_html
from .models import Contact,About,Skill,SkillChoice,Counter,CounterSection,Service,Summary_sec
from .models import EduDetail,EduCollege
from .models import ProfessionalWork,Pro_detail

admin.site.site_header="Portfolio"
admin.site.register(Skill)
admin.site.register(CounterSection)
admin.site.register(EduCollege)
admin.site.register(ProfessionalWork)


@admin.register(SkillChoice)
class SkillAdmin(admin.ModelAdmin):
    list_display=['id','skill_known','known_per']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','contact_date']
    list_display_links=['name']
    list_filter=['id','name','email']
    search_fields=['id','name','email']
    
@admin.register(About) 
class AboutAdmin(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html('<img src="{}" width="40" style="border-radius :50px;"/>'.format(obj.profile.url))
    thumbnail.short_description = 'user_profile'
    list_display=['id','thumbnail','age','website','phone','email','city','degree','freelance',]
    list_display_links=['website','email','city']
    list_editable=['freelance']
    search_fields=['email','phone']
    list_filter=['email','phone','city','website']

@admin.register(Counter)
class Counter(admin.ModelAdmin):
    list_display=['title','count']
    list_display_link=['count']
    
@admin.register(Service)  
class Service(admin.ModelAdmin):
    def thumbnail2(self,obj):
        return format_html('<img src="{}" width="40" style="border-radius :50px;"/>'.format(obj.service_img.url))
    thumbnail2.short_description = 'service_img'
    list_display=['service_name','thumbnail2','service_type','created_at']
    list_display_links=['service_type',]
    search_fields=['service_type']
    list_filter=['service_name','service_type']
    
    
    
# for Resumee section
@admin.register(Summary_sec)
class Summary_sec(admin.ModelAdmin):
    list_display=['id','about_name','about_email','about_phone']
    
    def about_name(self, obj):
        return obj.about_sum.name

    def about_email(self, obj):
        return obj.about_sum.email

    def about_phone(self, obj):
        return obj.about_sum.phone

    about_name.short_description = 'Name'
    about_email.short_description = 'Email'
    about_phone.short_description = 'Phone'
    
    
# eduaction section
# @admin.register(edu_details)
@admin.register(EduDetail)
class EducationAdmin(admin.ModelAdmin):
    list_display=['id','clg_name','clg_add','study_course','started_year','passed_year']
    list_display_links=['clg_name']
    search_fields=['clg_name','clg_add']
    list_filter=['clg_name']
    
    def clg_name(self,obj):
        return obj.clg_name.clg_name
    
    def clg_add(self,obj):
        return obj.clg_name.clg_add
    
    def study_course(self,obj):
        return obj.clg_name.study_course
    
    
    def started_year(self,obj):
        return obj.started_year
    
    def passed_year(self,obj):
        return obj.passed_year
    
    clg_name.short_description="College Name" 
    clg_add.short_description ="Location"
    study_course.short_description="Course" 
    started_year.short_description="Start Year" 
    passed_year.short_description="Pass Year" 
    

@admin.register(Pro_detail)
class Professional(admin.ModelAdmin):
    list_display=['id','Job_title','company_name','Job_location','started','end']
    list_display_links=['Job_title']
    search_fields=['Job_title','Job_location']
    # list_filter=['Job_title']
    
    def Job_title(self,obj):
        return obj.title.post
    
    
    def company_name(self,obj):
        return obj.company_name
    
    def Job_location(self,obj):
        return obj.work_location 
    
    def started(self,obj):
        return obj.work_start_date
    
    
    def end(self,obj):
        return obj.work_end_date
    
    Job_title.short_description="Job" 
    company_name.short_description="Company" 
    Job_location.short_description ="Address"
    started.short_description="Start" 
    end.short_description="End " 
    
