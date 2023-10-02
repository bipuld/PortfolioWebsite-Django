# Generated by Django 4.2.5 on 2023-10-02 15:56

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(default='', max_length=150)),
                ('title_desc', models.CharField(default='', max_length=150)),
                ('profile', models.ImageField(upload_to='profile')),
                ('birthdate', models.DateField()),
                ('website', models.URLField()),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(default='', max_length=150)),
                ('degree', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('freelance', models.BooleanField()),
                ('about_detail', ckeditor.fields.RichTextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', ckeditor.fields.RichTextField()),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CounterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_description', ckeditor.fields.RichTextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('mobile_dev', 'Mobile Development'), ('web_dev', 'Web Development'), ('cms', 'Content Management Systems'), ('responsive_design', 'Responsive Web Design'), ('ui_ux', 'UI/UX-Driven Development'), ('cross_platform', 'Cross-Platform Solutions'), ('e-commerce_solutions', 'E-commerce Solutions')], default='web_dev', max_length=50)),
                ('service_img', models.ImageField(default='', upload_to='service_photo')),
                ('service_name', models.CharField(max_length=150)),
                ('service_header', ckeditor.fields.RichTextField(default='')),
                ('service_desc', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Summary_sec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_intro', ckeditor.fields.RichTextField(default='')),
                ('about_sum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.about')),
            ],
        ),
        migrations.CreateModel(
            name='SkillChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('known_per', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('skill_known', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('count', models.PositiveIntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.countersection')),
            ],
        ),
    ]
