from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notices/', views.notices, name='notices'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('exam-schedule/', views.exam_schedule, name='exam_schedule'),
    path('ity/', views.ity, name='ity'),
]
