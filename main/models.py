from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# Assuming value is a string in ISO 8601 format
# value = "2023-09-28T15:30:00+00:00"
# dt = datetime.datetime.fromisoformat(value)


class Contact(models.Model):
    name=models.CharField(max_length=150)
    subject=models.CharField(max_length=200)
    email=models.EmailField()
    message=RichTextField()
    # contact_date=models.DateField(default=timezone.now(),blank=True)
    contact_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
    
    
class About(models.Model):
    name=models.CharField(max_length=150,blank=False,null=False)
    title=models.CharField(max_length=150,default="")
    title_desc=models.CharField(max_length=150,default="")
    profile=models.ImageField(upload_to="profile",)
    birthdate=models.DateField()
    website=models.URLField(max_length=200)
    phone=models.CharField(max_length=15)
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=150,default="")
    degree=models.CharField(max_length=50)
    email=models.EmailField()
    freelance=models.BooleanField(blank=False)
    about_detail=RichTextField(default="")
    
    # age=models.

    
    @property
    def age(self):
        today=datetime.now().date()
        delta=today-self.birthdate
        print(delta)
        print(delta.days)
        years = delta.days // 365
        return years
    def __str__(self):
        return f"{str(self.age)}     {self.name}"
    
# skills I know
class Skill(models.Model):
    name=models.CharField(max_length=150,null=False)
    
    def __str__(self):
        return self.name
    
class SkillChoice(models.Model):
    skill_known=models.ForeignKey(Skill,on_delete=models.CASCADE)
    known_per=models.PositiveIntegerField(
        validators=[
            MinValueValidator(5),
            MaxValueValidator(100),
        ]
    )
    def __str__(self):
        return f"{self.known_per} % of knowledge {self.skill_known} language "
    
    
class CounterSection(models.Model):
    counter_id=models.AutoField(primary_key=True)
    section_description=RichTextField(default="")
    def __str__(self):
        return self.section_description
    
class Counter(models.Model):
    section=models.ForeignKey(CounterSection,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} and Count:{self.count}" 
    
    
    
# for service 
class Service(models.Model):
    # service_img=models.ImageField(upload_to="service")
    SERVICE_CHOICES = (
        ('mobile_dev', 'Mobile Development'),
        ('web_dev', 'Web Development'),
        ('cms', 'Content Management Systems'),
        ('responsive_design', 'Responsive Web Design'),
        ('ui_ux', 'UI/UX-Driven Development'),
        ('cross_platform', 'Cross-Platform Solutions'),
        ('e-commerce_solutions', 'E-commerce Solutions'),
        
    )
    service_type=models.CharField(max_length=50,choices=SERVICE_CHOICES,default="web_dev")
    service_img=models.ImageField(upload_to="service_photo",default="")
    service_name=models.CharField(max_length=150)
    service_header=RichTextField(default="")
    service_desc=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f" {self.service_name}  {self.get_service_type_display()}"

# for resumee section

class Summary_sec(models.Model):
    about_sum=models.ForeignKey(About,on_delete=models.CASCADE)
    short_intro=RichTextField(default="")
    
    def __str__(self):
        return f"{self.about_sum.name}  {self.about_sum.email}  {self.about_sum.phone}  "
    
    
class EduCollege(models.Model):
    # id=models.AutoField(primary_key=True,default)
    id = models.AutoField(primary_key=True)

    study_course=models.CharField(max_length=200,default="")
    clg=models.CharField(max_length=150)
    clg_add=models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.clg

class EduDetail(models.Model):
    clg_name=models.ForeignKey(EduCollege,on_delete=models.CASCADE)   
    started_year=models.PositiveIntegerField(
        validators=[
            MinValueValidator(2010),
            MaxValueValidator(2999),
            ]
    )
    passed_year=models.PositiveIntegerField(
         validators=[
            MinValueValidator(2010),
            MaxValueValidator(2999),
        ]
    )
    inf_edu=RichTextField()
    
    
    def __str__(self):
        return f"{self.id}.{self.clg_name.clg} {self.started_year} - {self.passed_year}"

    
class ProfessionalWork(models.Model):
    post=models.CharField(verbose_name="YourPost",max_length=150)
    
    def __str__(self):
        return self.post

class Pro_detail(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.ForeignKey(ProfessionalWork,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200,default="")
    work_start_date = models.IntegerField(default=0)  # You may want to set an appropriate default value
    work_end_date = models.IntegerField(default=0)    # You may want to set an appropriate default value
    work_location = models.CharField(max_length=150, default="")  # You can set a default empty string or another value
    work_info = RichTextField()  # Assuming you're using CKEditor

    def __str__(self):
        return f"{self.title.post} {self.work_start_date} {self.work_location}"