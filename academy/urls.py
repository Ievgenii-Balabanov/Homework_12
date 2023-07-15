from academy import views

from django.urls import path

app_name = "academy"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("student/", views.StudentListView.as_view(), name="students_list"),
    path("student/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
    path("student/<int:pk>/studentprofile/", views.StudentProfileDetailView.as_view(), name="students_profile"),
    path("student/create/", views.StudentCreateView.as_view(), name="student_creation"),
    path("student/<int:pk>/update/", views.StudentUpdateView.as_view(), name="student_updating"),
    path("student/<int:pk>/delete/", views.StudentDeleteView.as_view(), name="student_delete"),
    # path("studentprofile/<int:pk>", views.StudentProfileDetailView.as_view(), name="students_profile"),
    path("subject/", views.SubjectListView.as_view(), name="subject_list"),
    path("subject/<int:pk>", views.SubjectDetailView.as_view(), name="subject_detail"),
    path("teacher/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teacher/<int:pk>", views.TeacherDetailView.as_view(), name="teacher_detail"),
    path("contact-us/", views.contact_us, name="contact-us"),
]
