from django import forms

from .models import Teacher, Group, Student


class GroupForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(
        queryset=Teacher.objects.all(), required=False
    )

    class Meta:
        model = Group
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 50:
            raise forms.ValidationError("Name is too long")
        if Group.objects.filter(name=name).exists():
            raise forms.ValidationError("This group already exists.")
        return name


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "birth_date", "groups"]


class TeacherDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True)


class StudentForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "group"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(last_name) > 50:
            raise forms.ValidationError("Surname is too long!")
        return last_name
