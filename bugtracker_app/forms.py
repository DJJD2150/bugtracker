from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from bugtracker_app.models import CustomUserModel, Ticket

# Create your forms here.
class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class TicketForm(forms.Form):
    title = forms.CharField(max_length=80)
    description = forms.CharField(widget=forms.Textarea)

class UserForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = CustomUserModel
        fields = ['bio']
