

from django.contrib.auth.models import AbstractUser
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model(models.Model):   # Scooter Model
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    scooter_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    scooter_model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    scooter_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

class MajorProblem(models.Model):
    WARNING_CHOICES = [
        ("battery", "Battery Issue 🔋"),
        ("motor", "Motor Issue ⚡"),
        ("temp", "Temperature 🌡️"),
        ("brake", "Brake Issue 🛑"),
        ("general", "General Fault ⚠️"),
    ]
    warning_type = models.CharField(max_length=50, choices=WARNING_CHOICES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.get_warning_type_display()} - {self.name}"

class ProblemReport(models.Model):
    WARNING_CHOICES = [
        ("battery", "Battery Issue 🔋"),
        ("motor", "Motor Issue ⚡"),
        ("temp", "Temperature 🌡️"),
        ("brake", "Brake Issue 🛑"),
        ("general", "General Fault ⚠️"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reports")
    problem_type = models.CharField(max_length=50, choices=WARNING_CHOICES)
    major_problem = models.ForeignKey(MajorProblem, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem_type} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

# models.py
class Solution(models.Model):
    problem_type = models.CharField(max_length=50)  # "battery", "brake", "motor"
    major_problem = models.ForeignKey(MajorProblem, on_delete=models.CASCADE)
    steps = models.TextField()  # Store as JSON string or plain text with line breaks
    image = models.ImageField(upload_to="solutions/images/", blank=True, null=True)
    video = models.FileField(upload_to="solutions/videos/", blank=True, null=True)
    voice = models.FileField(upload_to="solutions/voices/", blank=True, null=True)

    def get_steps(self):
        return self.steps.split("\n")  # If stored as plain text with line breaks
