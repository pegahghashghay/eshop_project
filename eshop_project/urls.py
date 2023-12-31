"""
URL configuration for eshop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('home/', include('home.urls')),
    path('articles/', include('article_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('products/', include('product_module.urls')),
    path('user/', include('user_panel_module.urls')),
    path('admin/', admin.site.urls, name='admin_site'),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth-token/', obtain_auth_token, name='generate_auth_token')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
