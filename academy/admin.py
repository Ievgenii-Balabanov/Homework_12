from django.contrib import admin
from .models import Student, StudentProfile, Subjects, Teacher, TeacherProfile


class ItemInLine(admin.StackedInline):
    model = Subjects
    extra = 2


class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_first_name", "student_last_name", "course"]
    fieldsets = [
        ("Last Name", {"fields": ["student_last_name"]}),
        ("Course", {"fields": ["course"]}),
        ("Teacher", {"fields": ["teacher"]}),
    ]

    search_fields = ["student_first_name"]
    list_filter = ["course"]
    filter_horizontal = ("teacher",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["teacher_last_name", "teacher_first_name", "seniority"]
    fieldsets = [
        ("Last Name", {"fields": ["teacher_last_name"]}),
        ("Seniority", {"fields": ["seniority"]}),
    ]

    inlines = [ItemInLine]

    search_fields = ["teacher_last_name"]
    list_filter = ["seniority"]


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ["subject_name", "lecture_amount"]
    fieldsets = [
        ("Subject", {"fields": ["subject_name"]}),
        ("Amount of lectures", {"fields": ["lecture_amount"]}),
        ("Students", {"fields": ["student_name"]}),
    ]
    filter_horizontal = ("student_name",)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentProfile)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherProfile)
