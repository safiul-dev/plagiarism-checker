from django.urls import path
from image_app import views
  
urlpatterns = [
    path('text-extract-image/',
         views.extractTextFromImage,
         name = 'text-extract-from-image'),
]