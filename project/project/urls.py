from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls'), name='tinymce'),
    path('users/', include('users.urls')),
    path('adverts/', include('advert.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
