
from django.contrib import admin
from django.urls import path, include, re_path
#from rest_framework.authtoken import views as AuthViews
from metrics.utils import custLogin
from metrics import views


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custLogin.CustomAuthToken.as_view()),
    re_path(r'^users', views.getUser),
    path('teams/', views.getTeams),
    path('tracks/', views.getTracks),
    re_path(r'^metrics/', include('pm.urls')),
    re_path(r'^sprint/', include('sm.urls'))
]

#urlpatterns = format_suffix_patterns(urlpatterns)
