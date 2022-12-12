
from django.urls import path
from plug import views
  
urlpatterns = [
    path('text-plagiarism/',
         views.checkPlagiarism,
         name = 'plag-check'),
]