from django.urls import path,include
from . import views
urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(),name="note-list"),
    path('notes/update/<int:pk>/',views.UpdateNote.as_view(),name='update-note'),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note')
]
