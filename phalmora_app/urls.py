from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('contact', views.contactpage, name='contact'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('software-development', views.software_development, name='software_development('),

    path('recruitment', views.recruitment, name='recruitment'),
    path('phalmorarecruiters', views.recruiters, name='recruiters'),
    path('contact', views.contactpage, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('recruitercontact', views.Recruitercontact, name='recruitercontact'),
    path('recruitercontact/', views.recruitercontact, name="recruiter_contact"),
    path('recruiterservices', views.RecruitersServices, name='recruiterservices'),
    path('recruiterabout', views.Recruiterabout, name='recruiterabout'),
    # path('service3', views.service3, name='service3'),
    # path('service4', views.service4, name='service4'),
    # path('service5', views.service5, name='service5'),
    # path('details', views.details, name='details'),
    # path("blogs/", views.blog_detail, name="blog_list"),
   
]
