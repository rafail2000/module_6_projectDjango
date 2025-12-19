from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
        FIRST_YEAR = 'first'
        SECOND_YEAR = 'second'
        THIRD_YEAR = 'third'
        FOURTH_YEAR = 'fourth'

        YEAR_IN_SCHOOL_CHOICES = [
                (FIRST_YEAR, 'Первый курс'),
                (SECOND_YEAR, 'Второй курс'),
                (THIRD_YEAR, 'Третий курс'),
                (FOURTH_YEAR, 'Четвёртый курс'),
        ]

        first_name = models.CharField(max_length=150, verbose_name='Имя')
        last_name = models.CharField(max_length=150, verbose_name='Фамилия')
        email = models.EmailField()
        year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICES, default=FIRST_YEAR, verbose_name='Курс')
        enrollment_date = models.DateTimeField()

        def __str__(self):
                return f'{self.first_name} {self.last_name}'

        class Meta:
                verbose_name = 'студент'
                verbose_name_plural = 'студенты'
                ordering = ['last_name',]