from django.shortcuts import render
from.models import Notes
from django.views.generic import CreateView ,ListView , DeleteView , UpdateView
from . forms import NotesForm
# Create your views here.
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model= Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

class NotesDetailView(DeleteView):
    model = Notes
    context_object_name = "note"


    

