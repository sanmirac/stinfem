from django.contrib import admin

from profiles.models import User, Student, Teacher, Parent

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
