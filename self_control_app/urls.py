from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notes/list/$', views.notesList, name='notes_list'),
    url(r'^notes/new/$', views.createNote, name='create_note'),
    url(r'^notes/(?P<note_id>[0-9]+)/$', views.note, name='note'),
    url(r'^notes/del/(?P<note_id>[0-9]+)/$', views.deleteNote, name='delete_note'),
    url(r'^notes/edit/(?P<note_id>[0-9]+)/$', views.editNote, name='edit_note'),
]