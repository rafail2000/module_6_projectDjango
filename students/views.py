from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from students.models import Student, MyModel


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'mymodel_form.html'
    success_url = reverse_lazy('mymodel')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'mymodel_list.html'
    context_object_name = 'mymodels'


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'mymodel_detail.html'
    context_object_name = 'mymodel'


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'mymodel_form.html'
    success_url = reverse_lazy('mymodel_list')


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'students/contact.html')


def example_view(request):
    return render(request, "students/example.html")


def index(request):
    student = Student.objects.get(id=1)
    context = {
        "student_name": f'{student.first_name} {student.last_name}',
        "student_year": student.get_year_display(),
    }
    return render(request, "students/index.html", context=context)


def students_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    contex = {"student": student}
    return render(request, "students/students_detail.html", contex)


def students_list(request):
    students = Student.objects.all()
    contex = {"students": students}
    return render(request, 'students/students_list.html', contex)
