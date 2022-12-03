from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('login/<int:id>/', views.login_detail, name="login_detail"),
    path('login/index', views.index, name='index'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name="signup"),
]
