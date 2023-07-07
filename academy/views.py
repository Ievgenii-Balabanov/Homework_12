from django.db.models import Count, Avg

from django.views import generic

from academy.models import Student, StudentProfile, Subjects, Teacher


class IndexView(generic.ListView):
    template_name = "academy/index.html"
    queryset = Student.objects.all()


class StudentListView(generic.ListView):
    model = Student
    template_name = "academy/students_list.html"
    queryset = Student.objects.prefetch_related("teacher").annotate(course_avg=Avg("course"))


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = "academy/student_detail.html"


class StudentProfileDetailView(generic.DetailView):
    model = StudentProfile
    template_name = "academy/student_profile.html"


class SubjectListView(generic.ListView):
    model = StudentProfile
    template_name = "academy/subject_list.html"
    queryset = Subjects.objects.select_related("teacher_name").annotate(student_count=Count("student_name__id"))


class SubjectDetailView(generic.DetailView):
    model = Subjects
    template_name = "academy/subject_detail.html"
    queryset = Subjects.objects.annotate(student_count=Count("student_name__id"))


class TeacherListView(generic.ListView):
    model = Teacher
    template_name = "academy/teacher_list.html"
    queryset = Teacher.objects.prefetch_related("subjects_set").all()


class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = "academy/teacher_detail.html"
