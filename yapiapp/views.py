# from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404
# from django.contrib.auth import login, logout, authenticate
# from .forms import NoteForm, RegisterForm, UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    queryset= Note.objects.all()
    serializer_class= NoteSerializer
    permission_classes= [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

    def get_queryset(self):
        return Note.objects.filter(user= self.request.user)
    

 

# class NoteList(APIView):
#     def get(self, request):
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class NoteDetail(APIView):
#     def get(self, request, pk):
#         note = get_object_or_404(Note, pk=pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         note = get_object_or_404(Note, pk=pk)
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         note = get_object_or_404(Note, pk=pk)
#         serializer = NoteSerializer(note, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         note = get_object_or_404(Note, pk=pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @login_required

# def add_note(request):
#     if request.method=='POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)  # don't save yet
#             note.user = request.user        # assign user to note
#             note.save() 
#             messages.success(request,'Note added successfully! ')
#             return redirect('note_list')
#     else:
#          form = NoteForm()

#     return render(request, 'yapiapp/add_note.html', {'form':form})

# @login_required

# def edit_note(request, pk):
#     note = get_object_or_404(Note, pk=pk)
#     if request.method == 'POST':
#         form = NoteForm(request.POST, instance= note)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Note updated successfully!')
#             return redirect('note_list')
#     else: 
#         form= NoteForm(instance=note)

#     return render(request, 'yapiapp/edit_note.html', {'form':form})

# @login_required
# def delete_note(request, pk):
#     note = get_object_or_404(Note, pk=pk)
#     if request.method== 'POST':
#         note.delete()
#         messages.success(request,'Note deleted successfully!')
#         return redirect('note_list')
#     return render(request, 'yapiapp/delete_note.html', {'note': note})


 

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             # Create the user
#             form.save()
#             # Display success message
#             messages.success(request, 'Account created successfully! You can now log in.')
#             # Redirect to login page
#             return redirect('login')  # Ensure this 'login' matches the URL name in urls.py
#         else:
#             # If form is invalid, display error message
#             print(form.errors)  # <--- Add this line for debugging

#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/register.html', {'form': form})