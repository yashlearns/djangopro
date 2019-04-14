
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.log_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.reg_user, name='register'),
]
