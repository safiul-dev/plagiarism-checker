
from django.urls import path
from plug import views
  
urlpatterns = [
    path('text-plagiarism/',
         views.twoTextPlagiarismCheck,
         name = 'text-plagiarism-check'),

    path('two-pdf-plagiarism-check/',
        views.twoPdfPlagiarismCheck,
        name= 'two-plagiarism-check')
]