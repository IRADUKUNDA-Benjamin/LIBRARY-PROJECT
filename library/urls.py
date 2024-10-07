from django.urls import path
from . import views

urlpatterns = [
   path('login/',views.loginpage,name='login'),
   path('loans/',views.loans,name='loans'),
   path('home/',views.home,name="home"),
   path('home/',views.loan_verifier,name="loan_verifier"),
   path('all_members/', views.all_members, name='all_members'),
   path('reg_member/',views.reg_member,name='reg_member'),
   #path('all_members/add/', views.add_member, name='add_member'),
   path('all_books/',views.all_books,name='all_books'),
   path('book_details/<int:id>',views.book_details,name='book_details'),
   path('member_details/<int:id>', views.member_details, name='member_details'),
   path('newloan',views.loan_registry,name='loan_reg'),
   path('loan_details/<int:id>',views.delete_loan, name="delete_loan"),
   path('reg_book/',views.reg_book,name="add_book"),
]
