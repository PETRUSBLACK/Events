from django.urls import path
from .import views

urlpatterns = [
    # path('', views.home, name=""),
    path('<int:year>/<str:month>/', views.home, name="home"),
]