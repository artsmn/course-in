from django.contrib import admin


# Register your models here.
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from course.models import Course, Lesson, Tutor, LessonNode, LessonNodeImage


class LessonNodeImageInline(NestedStackedInline):
    model = LessonNodeImage


class LessonNodeInline(NestedStackedInline):
    model = LessonNode
    inlines = (LessonNodeImageInline, )


class LessonInline(NestedStackedInline):
    model = Lesson
    inlines = (LessonNodeInline, )


@admin.register(Course)
class CourseAdmin(NestedModelAdmin):
    inlines = (LessonInline, )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    pass

