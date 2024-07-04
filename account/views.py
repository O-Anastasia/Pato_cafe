from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

class RegisterView(SuccessMessageMixin, CreateView):
    """
    Class for registration new users
    """
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
    success_message = "User was created successfully"

    def get_context_data(self, **kwargs) -> dict:
        """
        Add context data for register.html
        """
        context = super().get_context_data()

        context['comment_1'] = _('''
                                Donec quis euismod purus. Donec feugiat ligula rhoncus, 
                                varius nisl sed, tincidunt lectus. 
                                Nulla vulputate , lectus vel volutpat efficitur, 
                                orci lacus sodales sem, sit amet quam:
                                ''')
        context['phone'] = '(001) 345 6889'
        context['comment_2_line_1'] = _('Donec feugiat ligula rhoncus:')
        context['comment_2_line_2'] = _(', varius nisl sed, tinci-dunt lectus sodales sem.')
        context['register'] = _('Register')


        return context

class MyLoginView(LoginView):
    """
    Class for login new users
    """
    template_name = 'login.html'

    def get_success_url(self) -> HttpResponse:
        """
        Define URL after successful login
        """
        return self.request.GET.get('next', '/')



