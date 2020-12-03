from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from accounts.models import UserLesson
from course.models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/detail.html'


class CourseLessonsView(DetailView):
    model = Course
    template_name = 'course/lesson/lessons.html'

    def get_context_data(self, **kwargs):
        context = super(CourseLessonsView, self).get_context_data(**kwargs)

        context.update({
            'lessons': self.request.user.lessons
        })
        return context


class JoinCourseView(DetailView):
    model = Course

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        user = request.user
        if user.is_authenticated:
            user.join_course(course)
        return redirect('course:lessons', pk=course.pk)


class LessonView(DetailView):
    model = UserLesson
    template_name = 'course/lesson/lesson.html'


class FinishLessonView(View):

    def get(self, request, pk, **kwargs):
        lesson = UserLesson.objects.filter(user=request.user, lesson_id=pk)[0]
        lesson.completed = True
        lesson.save()
        return redirect('course:lessons', pk=lesson.lesson.course_id)


class LessonNodeView(DetailView):
    model = UserLesson
    template_name = 'course/lesson/lesson_node.html'

    def get(self, request, *args, **kwargs):
        self.node_id = kwargs.pop('node')
        return super(LessonNodeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LessonNodeView, self).get_context_data(**kwargs)
        context.update({
            'node': self.get_object().lesson.get_node(number=self.node_id)
        })
        return context
