from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from account.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import account.forms
import account.views

from .models import Note
from .forms import NoteForm
from .forms import SignupForm

# Котроллеры Note

@login_required()
def index(request):
    try:
        note = Note.objects.get(most_important=True, user=request.user)
    except ObjectDoesNotExist:
        note = None

    return render(request, 'index.html', {'important_note': note})

@login_required()
def notesList(request):
    notes = Note.objects.filter(user=request.user).order_by('-creation_date')
    return render(request, 'notes/list.html', {'notes': notes})

@login_required()
def note(request, note_id):
    note = get_object_or_404(Note, user=request.user, pk=note_id)
    return render(request, 'notes/show.html', {'note': note})

@login_required()
def createNote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Note()
            note = note.construct(
                form.cleaned_data['title'],
                form.cleaned_data['text'],
                form.cleaned_data['most_important'],
                form.cleaned_data['notification_send'], 
                request.user
            )
            note.save()

            return HttpResponseRedirect('/notes/'+str(note.id))
    else:
        form = NoteForm()

    return render(request, 'notes/create.html', {'form': form})

@login_required()
def editNote(request, note_id):
    note = get_object_or_404(Note, user=request.user, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = note.construct(
                form.cleaned_data['title'],
                form.cleaned_data['text'],
                form.cleaned_data['most_important'],
                form.cleaned_data['notification_send'],
                request.user
            )
            note.save()

            return HttpResponseRedirect('/notes/'+str(note.id))
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit.html', {'form': form, 'note': note})

@login_required()
def deleteNote(request, note_id):
    note = get_object_or_404(Note, user=request.user, pk=note_id)
    note.delete()

    return HttpResponseRedirect('/notes/list')


# Котроллеры myCash





# Котроллеры клиентов

class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):

    form_class = SignupForm

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        # do something
        super(SignupView, self).after_signup(form)