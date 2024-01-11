from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserDetailsForm,IncomeDetailsForm,ExpenseDetailsForm
from .models import UserDetails,Income,Expense
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Sum
from datetime import datetime
# Create your views here.
#----------------------Home Page -------------------------
def home(request):
  return render(request,'main/index.html')
def about(request):
  return render(request,'main/about.html')
#-------xxxxxxxxxx----------Home Page ----xxxxxxxxxxxx---------

#----------------------User Authentication ---------------------
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('summary'))  
            else:
                print("Account not Active")
        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request,'account/login.html')
  
def signup(request):
    registered=False
    if request.method == 'POST':
        user_form=UserDetailsForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form=UserDetailsForm()
    return render(request,'account/signup.html',{'fn':user_form})


@login_required
def user_logout(request):
    logout(request)
    return render(request,'main/index.html')

#---xxxxxxxxxxx-------User Authentication -----xxxxxxxxxxx-----

#---------------------Income Calculation ----------------------
def income(request):
  income_details=Income.objects.filter(user_info__user=request.user)
  total_income=Income.objects.filter(user_info__user=request.user).aggregate(Sum('income_Amount'))['income_Amount__sum'] or 0
  data={'category':[],'amount':[]}
  for i in income_details:
     data['category'].append(i.income_Category)
     data['amount'].append(float(i.income_Amount))
  if request.method=='POST':
     income_form=IncomeDetailsForm(request.POST)
     if income_form.is_valid():
        user_info, created=UserDetails.objects.get_or_create(user=request.user)
        income=income_form.save(commit=False)
        income.user_info=user_info
        income.save()
        return redirect('income')
  else:
     income_form=IncomeDetailsForm()
  return render(request,'income_details/income-details.html',{'form':income_form,'income_details':income_details,'total_income':total_income,'data':data})


def expense(request):
  expense_details=Expense.objects.filter(user_info__user=request.user)
  total_expense=Expense.objects.filter(user_info__user=request.user).aggregate(Sum('expense_Amount'))['expense_Amount__sum'] or 0
  data={'category':[],'amount':[]}
  for i in expense_details:
     data['category'].append(i.expense_Category)
     data['amount'].append(float(i.expense_Amount))
  if request.method=='POST':
     expense_form=ExpenseDetailsForm(request.POST)
     if expense_form.is_valid():
        user_info, created=UserDetails.objects.get_or_create(user=request.user)
        expense=expense_form.save(commit=False)
        expense.user_info=user_info
        expense.save()
        return redirect('expense')
  else:
   expense_form=ExpenseDetailsForm()
  return render(request,'income_details/expense.html',{'form':expense_form,'expense_details':expense_details,'total_expense':total_expense,'data':data})

def summary(request):
  today=datetime.today()
  current_month=today.month
  current_year=today.year
  income_details=Income.objects.filter(income_Date__month=current_month,income_Date__year=current_year,user_info__user=request.user)
  expense_details=Expense.objects.filter(expense_Date__month=current_month,expense_Date__year=current_year,user_info__user=request.user)
  monthly_income=Income.objects.filter(income_Date__month=current_month,income_Date__year=current_year,user_info__user=request.user).aggregate(Sum('income_Amount'))['income_Amount__sum'] or 0
  monthly_expense=Expense.objects.filter(expense_Date__month=current_month,expense_Date__year=current_year,user_info__user=request.user).aggregate(Sum('expense_Amount'))['expense_Amount__sum'] or 0
  monthly_saving=monthly_income-monthly_expense
  total_income=Income.objects.filter(user_info__user=request.user).aggregate(Sum('income_Amount'))['income_Amount__sum'] or 0
  total_expense=Expense.objects.filter(user_info__user=request.user).aggregate(Sum('expense_Amount'))['expense_Amount__sum'] or 0
  cash_amount=total_income-total_expense
  return render(request,'income_details/summary.html',{'income_details':income_details,'expense_details':expense_details,'monthly_income':monthly_income,'monthly_expense':monthly_expense,'monthly_saving':monthly_saving,'cash_amount':cash_amount,'current_month':today})

#---xxxxxxxxxxx-------Income Calculation -----xxxxxxxxxxx-----