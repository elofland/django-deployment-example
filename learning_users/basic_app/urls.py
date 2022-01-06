from django.urls import path
from basic_app import views

# TEMPLATE urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.user_login,name='user_login')
]
