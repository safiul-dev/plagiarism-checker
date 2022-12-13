
from django.urls import path
from plug import views
  
urlpatterns = [
    path('text-plagiarism/',
         views.twoTextPlagiarismCheck,
         name = 'plag-check'),
]