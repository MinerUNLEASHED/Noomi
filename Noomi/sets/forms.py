from django import forms
from sets.models import Sets

class new_set(forms.ModelForm):
    created_by = forms.CharField(required=False, widget=forms.HiddenInput)
    exclude = ['user',]
    class Meta():
        model = Sets
        fields = '__all__'
        
        
