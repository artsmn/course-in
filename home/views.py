from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from course.models import Course


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        courses = Course.objects.filter(is_active=True)
        ctx.update({
            'courses': courses
        })
        return ctx
