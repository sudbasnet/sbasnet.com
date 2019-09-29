from django.urls import path
from . import views

# for later
app_name = "unrestapp"

urlpatterns = [
    path('unrestapp/', views.unrestapp, name="unrestapp"),
]
