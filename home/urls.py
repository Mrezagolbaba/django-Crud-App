from django.urls import path
from . import views



urlpatterns=[
    path('email/', views.send_email),
    path('', views.home),
    path('detail/<int:todo_id>/',views.detail)
]