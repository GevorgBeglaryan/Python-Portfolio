from django.urls import path
from . import views

urlpatterns = [
    path('', views.programmer_list, name='programmer_list'),
    path('programmer/<int:pk>/', views.programmer_detail, name='programmer_detail'),
    path('add_programmer/', views.add_programmer, name='add_programmer'),
    path('programmer/<int:pk>/add_project/', views.add_project, name='add_project'),
]
