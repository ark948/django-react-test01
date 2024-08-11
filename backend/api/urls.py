from django.urls import path
from api import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]