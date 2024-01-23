from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path("",views.homepage ,name = "homepage"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    # ... other URL patterns ...
]
