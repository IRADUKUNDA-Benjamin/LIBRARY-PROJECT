from django.contrib import admin
from .models import Book, Member, Loan,Staff,Genre

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
   list_display=('name',)
class StaffAdmin(admin.ModelAdmin):
   list_display=('name','mail','password')
class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'price','ISBN', 'publication_date', 'available_copies')
class MemberAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'phone', 'membership_date')
class LoanAdmin(admin.ModelAdmin):
   list_display = ('book', 'member', 'loan_date', 'return_date','created_at','updated_at')

admin.site.register(Member, MemberAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Genre,GenreAdmin)

