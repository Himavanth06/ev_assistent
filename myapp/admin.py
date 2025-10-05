from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Brand, Model, MajorProblem, ProblemReport

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "scooter_brand", "scooter_model", "scooter_year", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("scooter_brand", "scooter_model", "scooter_year")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Model)
admin.site.register(Brand)

admin.site.register(MajorProblem)
admin.site.register(ProblemReport)
