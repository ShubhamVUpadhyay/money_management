from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('income/',views.income,name='income'),
    path('expense/',views.expense,name='expense'),
    path('summary/',views.summary,name='summary'),
]
