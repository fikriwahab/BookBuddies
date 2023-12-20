from django import forms
from katalog.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter authors'}),
            'average_rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter average rating'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN'}),
            'isbn13': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN 13'}),
            'language_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter language code'}),
            'num_pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of pages'}),
            'ratings_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating count'}),
            'text_review_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter text review count'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter publisher'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication date'}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Enter cover link'}),
        }