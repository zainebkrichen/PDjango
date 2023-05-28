
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin, auth
from arty import views
from artyprod import settings
from django.contrib.auth import views as auth_views
urlpatterns = [    
    path('admin/', admin.site.urls),
    path('arty/', include('arty.urls')),     
    path('accounts/', include('django.contrib.auth.urls')),                                       
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
