from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetails(models.Model):
  user=models.OneToOneField(User,on_delete=callable)
class Income(models.Model):
  Income_Categories=[
    ('salary','Salary/Wages'),
    ('freelance','Freelance/Consulting'),
    ('business','Business Income'),
    ('investment','Investment Returns'),
    ('gifts','Gifts/Donations'),
    ('side_hustles','Side Hustles'),
    ('rental','Rental Income'),
    ('interest','Interest and Dividends'),
    ('bonus','Bonus/Commisions'),
    ('other','Other'),
  ]
  user_info=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
  income_Category=models.CharField(max_length=20,choices=Income_Categories)
  income_Description=models.TextField(blank=True)
  income_Amount=models.DecimalField(max_digits=10,decimal_places=2)
  income_Date=models.DateField()

class Expense(models.Model):
  Expense_Categories=[
    ('housing','Housing'),
    ('childcare','Childcare'),
    ('transport','Transportation'),
    ('utlity','Utilities'),
    ('food','Food/Supplies'),
    ('pets','Pets'),
    ('savings','Savings'),
    ('entertainment','Entertainment'),
    ('healthcare','Healthcare'),
    ('insurance','Insurance'),
    ('personal','Personal Care'),
    ('debt','Debt'),
    ('gifts','Gifts'),
    ('donations','Donantions'),
    ('clothing','Clothing'),
    ('other','Other'),
  ]
  user_info=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
  expense_Category=models.CharField(max_length=20,choices=Expense_Categories)
  expense_Description=models.TextField(blank=True)
  expense_Amount=models.DecimalField(max_digits=10,decimal_places=2)
  expense_Date=models.DateField()
 
 
