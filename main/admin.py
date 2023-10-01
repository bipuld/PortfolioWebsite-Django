from django.contrib import admin
from .models import Contact,About,Skill,SkillChoice,Counter,CounterSection,Service
# from .models import Contact,About,Skill,SkillChoice
from django.utils.html import format_html
# Register your models here
admin.site.site_header="Portfolio"
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(CounterSection)



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