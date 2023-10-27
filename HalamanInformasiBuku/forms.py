from django import forms
from HalamanInformasiBuku.models import Loan


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['name', 'due_date']


