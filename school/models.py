from django.db import models


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    weight = models.PositiveIntegerField()
    teacher = models.ForeignKey('profiles.Teacher', related_name='subjects')
    students = models.ManyToManyField('profiles.Student',
                                      through='Grade',
                                      related_name='subjects')


class Grade(models.Model):
    # Connection table betweeb student and subject
    student = models.ForeignKey('profiles.Student')
    subject = models.ForeignKey(Subjects, related_name='grades')
    grade = models.CharField(max_length=255)


class Exam(models.Model):
    TYPE = (
        ('midterm', 'Midterm'),
        ('final', 'Final')
    )
    subject = models.ForeignKey(Subjects, related_name='exams')
    student = models.ManyToManyField('profiles.Student',
                                     through='ExamResult',
                                     related_name='exams')
    exam_type = models.CharField(choices=TYPE, max_length=255)


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, related_name='results')
    student = models.ForeignKey('profiles.Student',
                                related_name='exam_results')
    score = models.IntegerField()
