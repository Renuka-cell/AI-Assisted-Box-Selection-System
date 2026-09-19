from django.contrib import admin
from .models import Box


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "length",
        "width",
        "height",
        "max_weight",
        "cost",
    )
    search_fields = ("name",)