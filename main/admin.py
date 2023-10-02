from django.contrib import admin
from .models import Contact,About,Skill,SkillChoice,Counter,CounterSection,Service,Summary_sec
# from .models import Contact,About,Skill,SkillChoice
from django.utils.html import format_html
# Register your models here
admin.site.site_header="Portfolio"
admin.site.register(Skill)
admin.site.register(CounterSection)
# admin.site.register(Summary_sec)



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
    