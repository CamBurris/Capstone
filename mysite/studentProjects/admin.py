from django.contrib import admin
from studentProjects.models import Project, Student, ExtraForm

# Register your models here.
admin.site.register(Project)
admin.site.register(Student)
admin.site.register(ExtraForm)