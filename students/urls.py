from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("example/", views.example_view, name="example"),
    path("index/", views.index, name="index"),
    path("students_list/", views.students_list, name="students_list"),
    path("students_detail/<int:student_id>/", views.students_detail, name="students_detail"),
]