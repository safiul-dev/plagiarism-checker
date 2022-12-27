from django.urls import path
from google_search import views
  
urlpatterns = [
    path('text-google/',
         views.googleSearch,
         name = 'text-google-search'),
    path('get-some-data/',
         views.getSomeData,
         name="get-some-data"
        )
]