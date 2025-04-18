from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.

def note_list(request):
    notes= Note.objects.all()
    return render(request, 'yapiapp/note_list.html',{'notes':notes})


def add_note(request):
    if request.method=='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
         form = NoteForm()

    return render(request, 'yapiapp/add_note.html', {'form':form})