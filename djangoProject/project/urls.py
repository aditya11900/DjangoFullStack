from django.urls import path
from . import views

urlpatterns = [
    path('', views.project, name='all_projects'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
]