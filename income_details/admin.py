from django.contrib import admin
from . models import User,Income,Expense
# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)