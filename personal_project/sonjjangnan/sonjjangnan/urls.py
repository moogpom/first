
from django.contrib import admin
from django.urls import path,include
from introSon.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home,name="home"),
    path('admin/', admin.site.urls),
    path('introSon/',include('introSon.urls')),
    path('user/',include('user.urls')),
    path('accounts/',include('allauth.urls')),
    path('crud/',include('crud.urls')),
    #path('bookmark/',include('bookmark.urls')),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
