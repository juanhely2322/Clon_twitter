from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('register',views.register,name='register'),
   path('login',views.login_session,name='login'),
   path('logout',views.logout_session,name='logout'),
]


#from django.contrib.auth.views import LoginView, LogoutView #no olvidar importar
#otra forma de hacer login  path('login',LoginView.as_view(template_name='ubicacion_template'),name='login'),
"""urlpatterns = [
   path('register',views.register,name='register'),
   path('login',LoginView.as_view(template_name='twitter/login.html'),name='login'),
   path('logout',LogoutView.as_view(),name='logout'),
]"""