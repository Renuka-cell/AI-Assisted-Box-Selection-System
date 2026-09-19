from django.urls import path
from .views import (
    BoxListCreateView,
    BoxDetailView,
)

urlpatterns = [
    path(
        "",
        BoxListCreateView.as_view(),
        name="box-list-create"
    ),
    path(
        "<int:pk>/",
        BoxDetailView.as_view(),
        name="box-detail"
    ),
]