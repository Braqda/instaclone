from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

BASE_INPUT_CLASSES = (
    'w-full px-4 py-2 text-sm bg-gray-50 border border-gray-200 rounded-xl '
    'focus:outline-none focus:ring-2 focus:ring-purple-500 focus:bg-white transition-all'
)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Tell us about yourself...',
                'class': BASE_INPUT_CLASSES + ' resize-none',
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': (
                    'block w-full text-xs text-gray-500 file:mr-4 file:py-2 file:px-4 '
                    'file:rounded-full file:border-0 file:text-xs file:font-semibold '
                    'file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100 cursor-pointer'
                ),
            }),
        }
