from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import CustomUserCreationForm, ProblemReportForm
from .models import CustomUser, Brand, Model, MajorProblem, ProblemReport
from .solutions import SOLUTIONS
from .solutions import get_solution



# -------------------------------
# AJAX / Dynamic Data Load
# -------------------------------

def load_models(request):
    """Return models for a selected brand via AJAX."""
    brand_id = request.GET.get("brand_id")
    models = Model.objects.filter(brand_id=brand_id).values("id", "name")
    return JsonResponse(list(models), safe=False)



def load_major_problems(request):
    warning_type = request.GET.get("warning_type")
    # Exclude temperature entirely
    if warning_type.lower() == "temperature":
        return JsonResponse([], safe=False)

    problems = MajorProblem.objects.filter(warning_type=warning_type).values("id", "name")
    return JsonResponse(list(problems), safe=False)



# -------------------------------
# Authentication Views
# -------------------------------

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            login(request, user)
            return redirect("dashboard")
        else:
            print(form.errors)  # Display errors in terminal
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# -------------------------------
# Main App Views
# -------------------------------

def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def past_reports(request):
    """Show user's past problem reports (template not yet created)."""
    reports = ProblemReport.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "past_reports.html", {"reports": reports})


@login_required
def report_problem(request):
    """Submit a new problem report."""
    if request.method == "POST":
        form = ProblemReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("problem_solution", report_id=report.id)
    else:
        form = ProblemReportForm()
    return render(request, "report_problem.html", {"form": form})


@login_required
#from .solutions import get_solution   # add this import


@login_required
def problem_solution(request, report_id):
    report = get_object_or_404(ProblemReport, id=report_id)
    major_name = report.major_problem.name if report.major_problem else None

    # Use the helper that normalizes keys
    solution = get_solution(report.problem_type, major_name)

    return render(request, "solution.html", {"report": report, "media": solution})
