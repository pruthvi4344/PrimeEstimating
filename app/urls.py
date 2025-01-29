from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('login', views.admin_login, name='admin_login'),
    path('logout',views.admin_logout, name='admin_logout'),
    path('delete-service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('edit-service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('about/edit/', views.edit_about, name='edit_about'),
    path('about/delete/', views.delete_about, name='delete_about'),
    path('contact/edit/', views.edit_contact, name='edit_contact'),
    path('contact/delete/', views.delete_contact, name='delete_contact'),
    path('indexmanage/edit/', views.edit_indexmanage, name='edit_indexmanage'),
    path('indexmanage/delete/', views.delete_indexmanage, name='delete_indexmanage'),
    path('servicemanage/edit/', views.edit_servicemanage, name='edit_servicemanage'),
    path('servicemanage/delete/', views.delete_servicemanage, name='delete_servicemanage'),
    path('aboutmanage/edit/', views.edit_aboutmanage, name='edit_aboutmanage'),
    path('aboutmanage/delete/', views.delete_aboutmanage, name='delete_aboutmanage'),
    path('contactmanage/edit/', views.edit_contactmanage, name='edit_contactmanage'),
    path('contactmanage/delete/', views.delete_contactmanage, name='delete_contactmanage'),

]