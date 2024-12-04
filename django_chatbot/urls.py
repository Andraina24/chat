from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),  # Inclut les vues d'authentification par défaut de Django
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path('', include('chatbot.urls')),  # Remplace 'chatbot' par le nom de ton application si nécessaire
]
