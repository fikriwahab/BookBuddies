from __future__ import with_statement
from django import forms
from HalamanInformasiBuku.models import Loan
from typing import Text

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['name', 'due_date', 'address']  # Daftar field yang harus dimasukkan

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Menambahkan atribut widget untuk menyesuaikan tampilan
            'due_date': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }