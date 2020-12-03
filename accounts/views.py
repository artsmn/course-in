from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from accounts.forms import SignInForm, SignUpForm
from accounts.models import User


class SignInView(FormView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = User.objects.get(email=form.data.get('email'))
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class SignUpView(FormView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        user = User.objects.get(email=form.data.get('email'))
        user.set_password(form.data.get('password'))
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))
