from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'target_streak']  # Add optional fields
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'target_streak': forms.NumberInput(attrs={'min': 1}),
        }
