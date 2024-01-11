from .models import UserDetails,Income,Expense
from django import forms
from django.contrib.auth.models import User

class UserDetailsForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),help_text=None)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta():
        model=User
        fields=('username','password','email')

class IncomeDetailsForm(forms.ModelForm):
    income_Date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=Income
        fields=['income_Category','income_Description','income_Amount','income_Date']
        widgets={
            'income_Description': forms.Textarea(attrs={'cols':50,'rows':5})
        }

class ExpenseDetailsForm(forms.ModelForm):
    expense_Date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=Expense
        fields=['expense_Category','expense_Description','expense_Amount','expense_Date']
        widgets={
            'expense_Description': forms.Textarea(attrs={'cols':50,'rows':5})
        }
