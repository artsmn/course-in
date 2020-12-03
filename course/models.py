from django.db import models


# Create your models here.
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404


class Tutor(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.full_name


class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name='Course name')
    description = models.TextField(verbose_name='Course description')
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, verbose_name='Tutor', null=True)
    image = models.ImageField(null=True)
    is_active = models.BooleanField(verbose_name='Is Active')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=128, verbose_name='Lessons name')
    description = models.TextField(verbose_name='Lesson description')

    def get_first_node(self):
        return self.nodes.order_by('number')[0]

    def get_node(self, number):
        return get_object_or_404(LessonNode, lesson=self, number=number)


class LessonNode(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='nodes')
    number = models.IntegerField()
    text = models.TextField(verbose_name='Text')

    def is_last(self):
        return self.lesson.nodes.order_by('number').last() == self

    def is_first(self):
        return self.lesson.nodes.order_by('number').first() == self

    def get_next_node(self):
        nodes = self.lesson.nodes.order_by('number')
        index = list(nodes.values_list('id', flat=True)).index(self.id)
        if not self.is_last():
            return nodes[index + 1]

    def get_previous_node(self):
        nodes = self.lesson.nodes.order_by('number')
        index = list(nodes.values_list('id', flat=True)).index(self.id)
        if not self.is_first():
            return nodes[index - 1]


class LessonNodeImage(models.Model):
    name = models.CharField(verbose_name="Image name", max_length=256)
    image = models.ImageField(upload_to='lesson_image/')
    lesson_node = models.ForeignKey(LessonNode, on_delete=models.CASCADE, related_name='images')
