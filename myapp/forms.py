
from .models import Activities, ActivityReply, File, Meeting, Reply
from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'content']

class ActivityReplyForm(forms.ModelForm):
    class Meta:
        model = ActivityReply
        fields = ['author', 'content']

class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['author', 'name', 'type', 'startTime', 'endTime', 'location', 'description']

class CreateMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['author', 'name', 'numParticipants', 'participantNames']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'filepath']