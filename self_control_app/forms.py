from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
import account.forms

from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'most_important', 'notification_send']
        widgets = {
            'text': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}})
        }


class SignupForm(account.forms.SignupForm):
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]