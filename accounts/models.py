from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db.models import Count, Q

from course.models import Course


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=128, verbose_name="First Name", null=True)
    last_name = models.CharField(max_length=128, verbose_name="Last Name", null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    username = models.CharField(unique=True, null=True, verbose_name="Username", max_length=128, blank=True)
    courses = models.ManyToManyField('course.Course', blank=True)

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return '{user.first_name} {user.last_name}'.format(user=self)
        else:
            return self.email

    @property
    def lessons(self):
        return UserLesson.objects.filter(user=self)

    @property
    def not_joined_courses(self):
        courses = Course.objects.filter(is_active=True).exclude(user=self)
        return courses

    @property
    def unfinished_courses(self):
        return Course.objects.annotate(lessons_count=Count('lessons'))\
            .filter(lessons__userlesson__user=self)\
            .exclude(lessons_count=Count('lessons', filter=Q(lessons__userlesson__completed=True)))

    @property
    def completed_courses(self):
        return Course.objects.annotate(lessons_count=Count('lessons'))\
            .filter(lessons__userlesson__user=self,
                    lessons_count=Count('lessons', filter=Q(lessons__userlesson__completed=True)))

    def join_course(self, course):
        self.courses.add(course)
        UserLesson.objects.bulk_create(objs=[
            UserLesson(user=self, lesson=lesson) for lesson in course.lessons.all()
        ])

    def __str__(self):
        return self.full_name


class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey('course.Lesson', on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)
