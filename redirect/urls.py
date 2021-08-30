from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
				path('',views.portaLogin,name='landingPageLogin'),
				path('redirectLandingPage/',login_required(views.redirectLandingPage),name='redirectLandingPage'),
				path('500/<str:redirect_url>/',login_required(views.generic500page),name='generic500page'),	
			]

from django.urls import re_path
urlpatterns += [
    re_path(r'^accounts/login/', views.portaLogin, name='landingPageRedirectlogin'),
    re_path(r'logout/', views.portalLogout, name='portaLogout'),
]