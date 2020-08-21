from django import forms
from ghostapp.models import BoastRoast


class NewPost(forms.Form): #Helped by Sohail
    CHOICES = [(True, 'boast'),(False, 'roast')]
    boast = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, help_text="Please Select One")
    create_post = forms.CharField(max_length=280, widget=forms.Textarea)

    
        
    
