from django import forms
from .models import JobSeeker


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['cv', 'requirements']
