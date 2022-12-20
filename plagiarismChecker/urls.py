
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls')),
    path('api/', include('plug.urls')),
    path('api/', include('image_app.urls')),
    path('api/', include('google_search.urls'))
]
