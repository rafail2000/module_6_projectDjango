from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.urls import reverse_lazy

from students.forms import StudentForm
from .models import Student, MyModel

from django.core.cache import cache


def my_view(request):
    data = cache.get('my_key')

    if not data:
        data = 'some expensive computation'
        cache.set('my_key', data, 60 * 15)

    return HttpResponse(data)


class PromoteStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('students.can_promote_student'):
            return HttpResponseForbidden("У вас нет прав для перевода студента.")

        student.year = next_year(student.year)
        student.save()

        return redirect('students:student_list')


class ExpelStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('students.can_expel_student'):
            return HttpResponseForbidden("У вас нет прав для исключения студента.")

        student.delete()

        return redirect('students:student_list')


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name =  'students/student_list.html'
    context_object_name =  'students'

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student'):
            return Student.objects.none()
        return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:students_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:students_list')


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['error_message'] = 'Please correct the errors'


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

    def get_queryset(self):
        return MyModel.objects.filter(is_activ=True)


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

    def get_additional_data(self):
        return "Это дополнительная информация"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = self.get_additional_data()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.is_active:
            raise Http404("Object not found")
        return obj


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
