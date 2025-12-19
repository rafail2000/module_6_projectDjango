from django import forms
from django.core.exceptions import ValidationError

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "year", "email", "enrollment_date"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith('@example.com'):
            raise ValidationError("Email должен заканчиваться на @example.com")
        return email

    def clean(self):
        cleaned_data  = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name == last_name:
            self.add_error("last_name", "Имя и фамилия не могут иметь одинаковые значения")