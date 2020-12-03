from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('<int:pk>/',  views.CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/lessons/',  views.CourseLessonsView.as_view(), name='lessons'),
    path('<int:pk>/join/',  views.JoinCourseView.as_view(), name='join'),
    path('lessons/<int:pk>/', views.LessonView.as_view(), name='lesson'),
    path('lessons/<int:pk>/nodes/<int:node>/', views.LessonNodeView.as_view(), name='lesson_node'),
    path('lessons/<int:pk>/finish/', views.FinishLessonView.as_view(), name='lesson_finish')
]
