from django.contrib import admin

from school.models import Subjects, Grade, Exam, ExamResult

admin.site.register(Subjects)
admin.site.register(Grade)
admin.site.register(Exam)
admin.site.register(ExamResult)
