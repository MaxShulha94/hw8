from django.urls import path
from .views import teacher_form, group_form, teacher_list, group_list, teacher_edit, group_edit, student_list, student_form\
    , student_edit

urlpatterns = [
    path("group/", group_form, name="group_form"),
    path("groups/", group_list, name="groups_list"),
    path("group_edit/<int:pk>", group_edit, name="group_edit"),
    path("teacher/", teacher_form, name="teacher_form"),
    path("teachers/", teacher_list, name="teacher_list"),
    path("teacher_edit/<int:pk>", teacher_edit, name="teacher_edit"),
    path("student/", student_form, name="student_form"),
    path("students/", student_list, name="student_list"),
    path("student_edit/<int:pk>", student_edit, name="student_edit")
]