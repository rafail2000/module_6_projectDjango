from django.urls import path
from . import views
from .views import MyModelListView, MyModelDetailView, MyModelCreateView, MyModelUpdateView, MyModelDeleteView

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("example/", views.example_view, name="example"),
    path("index/", views.index, name="index"),
    path("student/", views.students_list, name="students_list"),
    path("students_detail/<int:student_id>/", views.students_detail, name="students_detail"),
    path("student/create/", views.StudentCreateView.as_view(), name="student_create"),
    path("student/update/<int:pk>/", views.StudentUpdateView.as_view(), name="student_update"),


    path('mymodel/', MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/<int:pk>/', MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/new/', MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/<int:pk>/edit/', MyModelUpdateView.as_view(), name='mymodel_edit'),
    path('mymodel/<int:pk>/delete/', MyModelDeleteView.as_view(), name='mymodel_delete'),
]