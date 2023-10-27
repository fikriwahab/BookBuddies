from django import forms
from HalamanInformasiBuku.models import Book, Bookmark, BookReview, Loan

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['text']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['name', 'due_date']

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = []
