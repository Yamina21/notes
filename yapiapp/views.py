from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import Note
from .forms import NoteForm, RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required

def note_list(request):
    notes= Note.objects.all()
    return render(request, 'yapiapp/note_list.html',{'notes':notes})

@login_required

def add_note(request):
    if request.method=='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # don't save yet
            note.user = request.user        # assign user to note
            note.save() 
            form.save()
            return redirect('note_list')
    else:
         form = NoteForm()

    return render(request, 'yapiapp/add_note.html', {'form':form})

@login_required

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance= note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else: 
        form= NoteForm(instance=note)

    return render(request, 'yapiapp/edit_note.html', {'form':form})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method== 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'yapiapp/delete_note.html', {'note': note})


def register_view(request):
    if request.method =='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})