from django.urls import path
from users import views
app_name='users'
from django.contrib.auth import views as aviews 
urlpatterns = [
    path('register/',views.register_user,name='user'),
    path('login/',aviews.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/',views.profile,name='profile')
]
