from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedViews.as_view()),
    path('signup/login/',views.LoginInterfaceView.as_view(), name='login'),
    path('logout/',views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/',views.Signupview.as_view(), name='signup'),
]