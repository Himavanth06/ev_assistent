from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Brand, Model, ProblemReport, MajorProblem


# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "scooter_brand",
            "scooter_model",
            "scooter_year",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["scooter_brand"].queryset = Brand.objects.all()
        self.fields["scooter_model"].queryset = Model.objects.none()

        if "scooter_brand" in self.data:
            try:
                brand_id = int(self.data.get("scooter_brand"))
                self.fields["scooter_model"].queryset = Model.objects.filter(brand_id=brand_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["scooter_model"].queryset = Model.objects.filter(brand=self.instance.scooter_brand)


# Problem Report Form
class ProblemReportForm(forms.ModelForm):
    class Meta:
        model = ProblemReport
        fields = ["problem_type", "major_problem", "description"]
        widgets = {
            "problem_type": forms.Select(attrs={"class": "form-select"}),
            "major_problem": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Describe your issue here...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Exclude temperature from problem_type dropdown
        original_choices = self.fields["problem_type"].choices
        self.fields["problem_type"].choices = [
            (val, label) for val, label in original_choices if val != "temperature"
        ]

        # Start with empty major_problem queryset
        self.fields["major_problem"].queryset = MajorProblem.objects.none()

        if "problem_type" in self.data:
            try:
                warning_type = self.data.get("problem_type")
                self.fields["major_problem"].queryset = MajorProblem.objects.filter(warning_type=warning_type)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["major_problem"].queryset = MajorProblem.objects.filter(
                warning_type=self.instance.problem_type
            )
    