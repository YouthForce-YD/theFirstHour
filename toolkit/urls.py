from django.urls import path
from . import views

app_name = 'toolkit'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('situation/<slug:slug>/', views.situationDetailView, name='situationDetail'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('action/save-incident/', views.saveIncidentAction, name='saveIncident'),
    path('action/delete-incident/<int:reportId>/', views.deleteIncidentView, name='deleteIncident'),
]
