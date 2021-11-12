from django.urls import path
from complaint_app.views import ComplaintCreationSuccessful, homePageView, LoginView, SignUpView, CreateComplaintView

urlpatterns = [
    path('', homePageView, name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('create/', CreateComplaintView.as_view(), name="create_complaint"),
    path('success/', ComplaintCreationSuccessful.as_view(), name="created_successfully")
]
