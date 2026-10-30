from django import forms
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [
            'title',
            'subject',
            'description',
            'file',
            'due_date',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter assignment title'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter subject name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter assignment details',
                'rows': 4
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')

        if uploaded_file:
            allowed_extensions = [
                '.pdf', '.doc', '.docx', '.txt'
            ]
            import os

            extension = os.path.splitext(
                uploaded_file.name
            )[1].lower()

            if extension not in allowed_extensions:
                raise forms.ValidationError(
                    'Only PDF, DOC, DOCX and TXT files are allowed.'
                )

            if uploaded_file.size > 10 * 1024 * 1024:
                raise forms.ValidationError(
                    'File size must be less than 10 MB.'
                )

        return uploaded_file