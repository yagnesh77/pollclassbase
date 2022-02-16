from django.contrib import admin
from django.urls import path
from . import views

# django admin header customization

admin.site.site_header =" Login To Developer Yagnesh"
admin.site.site_title ="Welcome to yagnesh's Dashboard"
admin.site.index_title ="Welcome To Yagnesh's Admin Panel "

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:question_id>', views.detail.as_view(), name='detail'),
    path('<int:question_id>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote.as_view(), name='vote'),
    path('contact', views.contact.as_view(), name='contact'),
    
]
