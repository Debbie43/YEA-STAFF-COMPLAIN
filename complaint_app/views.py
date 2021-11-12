from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from complaint_app.models import Complaint

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World')

class SignUpView(TemplateView):
    template_name = 'sign_up.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class CreateComplaintView(CreateView):
    model = Complaint
    template_name = 'create_complaint.html'
    fields = ['name','directorate', 'location', 'device', 'problem', 'short_description']

    def get_success_url(self) -> str:
        return 'success/'

class ComplaintCreationSuccessful(TemplateView):
    template_name = 'complaint_creation_successful.html'