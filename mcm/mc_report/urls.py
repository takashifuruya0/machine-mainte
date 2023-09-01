from django.urls import path
from . import views

urlpatterns = [
    path('', views.l1_list, name='l1_list'),
    path('<int:pk>/', views.issue_list, name='issue_list'),
    path('', views.post_issue, name='post_issue'),
]