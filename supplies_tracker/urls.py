from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "supplies_tracker"
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('request/<int:pk>/update/', views.UpdateShipmentRequestView.as_view(), name='update_request'),
    path('login/', auth_views.LoginView.as_view(template_name='supplies_tracker/login.html', redirect_field_name="next"),name='user_login'),
]
