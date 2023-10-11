from django.db import models



class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    groups = models.ManyToManyField(Group, related_name="groups")

    def __str__(self):
        return f"Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.birth_date};"



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(
        Group, on_delete=models.PROTECT, related_name="students", default=None
    )

    def __str__(self):
        return f"Name: {self.first_name}, Surname: {self.last_name};"
