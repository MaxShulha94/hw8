from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import GroupForm, TeacherForm, StudentForm

from .models import Group, Teacher, Student


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("teacher_list"))

    return render(request, "teacher_form.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})

    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()

        return redirect("teacher_list")
    return render(request, "teacher_edit.html", {"form": form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect("teacher_list")


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("groups_list"))

    return render(request, "group_form.html", {"form": form})


def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(request, "group_edit.html", {"form": form})

    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        form.instance.teacher.clear()
        form.instance.teacher.set(form.cleaned_data["teacher"])
        form.save()
        return redirect(reverse("group_edit", args=[pk]))

    return render(request, "group_edit.html", {"form": form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect("group_list")


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})
    form = StudentForm(request.POST, request.FILES)
    if form.is_valid():
        group_id = request.POST["group"]
        group_id = Group.objects.get(pk=group_id)
        s = form.save(commit=False)
        s.group = group_id
        s.save()
        return redirect(reverse("student_list"))
    return render(request, "student_form.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "student_form.html", {"form": form})


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")
