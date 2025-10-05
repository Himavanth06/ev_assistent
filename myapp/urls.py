from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("report-problem/", views.report_problem, name="report_problem"),  # placeholder
    path("past-reports/", views.past_reports, name="past_reports"), 
    path("logout/", views.logout_view, name="logout"),
    path("ajax/load-models/", views.load_models, name="ajax_load_models"), 
    path("ajax/load-major-problems/", views.load_major_problems, name="ajax_load_major_problems"),
    path("solution/<int:report_id>/", views.problem_solution, name="problem_solution"),
 # AJAX endpoint
]


