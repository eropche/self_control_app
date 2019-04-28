from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField('date created')
    most_important = models.BooleanField(default=False)
    notification_send = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def construct(self, title, text, most_important, notification_send, user):
        self.title = title
        self.text = text
        if (most_important):
            try:
                important_note = Note.objects.get(most_important=True)
                important_note.most_important = False
                important_note.save()
            except ObjectDoesNotExist:
                important_note = None
        if (self.id == None):
            self.creation_date = datetime.now()
            
        self.most_important = most_important
        self.notification_send = notification_send
        self.user = user

        return self

class MyCash(models.Model):
    category = models.CharField(max_length=200)
    date = models.DateTimeField()
    remind = models.BooleanField(default=False)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def construct(self, category, date, remind, money, user):
        self.category = category
        self.date = date
        self.remind = remind
        self.money = money
        self.user = user

        return self