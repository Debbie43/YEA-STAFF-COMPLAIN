from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World')

class SignUpView(TemplateView):
    template_name = 'sign_up.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class CreateComplaintView(TemplateView):
    template_name = 'create_complaint.html'

class ComplaintCreationSuccessful(TemplateView):
    template_name = 'complaint_creation_successful.html'