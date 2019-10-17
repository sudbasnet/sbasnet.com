from django.urls import path
from . import views

# for later
app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('rocket/', views.rocket, name="rocket"),

]
