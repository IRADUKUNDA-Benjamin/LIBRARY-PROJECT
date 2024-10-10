from django.shortcuts import render, redirect,get_object_or_404
from .models import Book, Member, Loan, Staff,Genre
from django.http import HttpResponse
from django.template import loader
from .forms import MemberForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime,date

# Create your views here.
def home(request):
   template=loader.get_template("home.html")
   context={

   }
   return HttpResponse(template.render(context, request))

def all_members(request):
   mymembers=Member.objects.all()
   template=loader.get_template("all_members.html")
   context={
      'mymembers': mymembers,
   }
   return HttpResponse(template.render(context,request))


def member_details(request,id):
   members=Member.objects.get(id=id)
   template=loader.get_template('member_details.html')
   context={
      'mem':members
   }
   return HttpResponse(template.render(context, request))
   
def all_books(request):
   books=Book.objects.all()
   template=loader.get_template('all_books.html')
   context={
      'books':books
   }
   return HttpResponse(template.render(context,request))

def book_details(request, id):
   obj=Book.objects.all().get(id=id)
   template=loader.get_template('book_details.html')
   context={
      'obj':obj
   }
   return HttpResponse(template.render(context,request))

def loginpage(request):
   
   if request.method=='POST':
      email=request.POST.get('email')
      password=request.POST.get('password')

      try:
         user=Staff.objects.get(mail=email)
      except:
         messages.error(request, 'user does not exist')
         return redirect('login')
      else:
         return redirect('home')

      
   template=loader.get_template('loginpage.html')
   context={

   }
   return HttpResponse(template.render(context,request))

def loan_registry(request):
   if request.method=='POST':
      membername=request.POST.get('membername')
      title=request.POST.get('title')
      email=request.POST.get('member_email')
      loan_date_str=request.POST.get('loan_date')
      return_date_str=request.POST.get('return_date')
      

   
      try:
         loan_date=datetime.strptime(loan_date_str,'%Y-%m-%d').date()
         return_date=datetime.strptime(return_date_str,'%Y-%m-%d').date()
         member=Member.objects.get(name=membername)
         book=Book.objects.get(title=title)
      except Book.DoesNotExist:
         messages.error(request,"Book is not available")
         return redirect('loan_reg')

      except Member.DoesNotExist:
         messages.error(request,"this member is not registered")
         return redirect ('loan_reg')
      except ValueError:
         messages.error(request,"check  your date please")
         return redirect ('loan_reg')
      else:
         loan=Loan(book=book,member=member,loan_date=loan_date,return_date=return_date)
         loan.save()
         book.available_copies=book.available_copies-1
         messages.success(request, "Book loaned succesfully")
         
   template=loader.get_template('newloan.html')
   context={

   }
   return HttpResponse(template.render(context,request))


def loan_verifier(request):
   today = timezone.now().date()
   three_days_ago = today - timedelta(days=3)
   recent_books = Loan.objects.filter(loan_date__gte=three_days_ago, loan_date__lte=today)
   overdue_books = Loan.objects.filter(return_date__lt=today)
   context = {
      'recent_books': recent_books,
      'overdue_books': overdue_books,
   }
   return render(request, 'home.html', context)

def loans(request):
   myloans=Loan.objects.all()
   member=Member.objects.all()
   book=Book.objects.all()
   template=loader.get_template('loans.html')
   context={
      'myloans':myloans,
      'member':member
   }
   return HttpResponse(template.render(context,request))

def reg_member(request):
   if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      phone=request.POST.get('telephone')
      membership_date=date.today()
      
      try:
         existing=Member.objects.all().get(email=email)
      except Member.DoesNotExist:
         member=Member(name=name,email=email,phone=phone,membership_date=membership_date)
         member.save()
      else:
         messages.error(request,"member is arleady registered")
      
   template=loader.get_template('reg_member.html')
   context={}
   return HttpResponse(template.render(context,request))

def delete_loan(request, id):

    loa = get_object_or_404(Loan, id=id)

    if request.method == 'POST':
 
        loa.delete()
        messages.success(request, "Loan removed successfully")
        return redirect('home')     

    context = {
        'loa': loa, 
    }

    return render(request, 'loan_details.html', context)

def reg_book(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      author = request.POST.get('author')
      genre_name = request.POST.get('genre')
      price = request.POST.get('price')
      ISBN = request.POST.get('ISBN')
      publication_date_str = request.POST.get('publication_date')
      available_copies = request.POST.get('available_copies')

      try:
         existing_book = Book.objects.get(ISBN=ISBN)
         messages.error(request, "Book is already registered")
         return redirect('reg_book')
      except Book.DoesNotExist:
         try:
                # Parse the publication date
            publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d').date()
         except ValueError:
            messages.error(request, "Invalid date format for publication date")
            return redirect('reg_book')

         try:
                # Find the genre object based on the genre name
            genre = Genre.objects.get(name=genre_name)
         except Genre.DoesNotExist:
            messages.error(request, "Genre not found")
            return redirect('reg_book')

            # Create a new Book instance and save it
         book = Book(
            title=title,
            author=author,
            genre=genre,
            price=price,
            ISBN=ISBN,
            publication_date=publication_date,
            available_copies=available_copies
            )
         book.save()
         messages.success(request, "Book was successfully registered")
         return redirect('reg_book')

    # Fetch all genres to display in the datalist
   genres = Genre.objects.all()
   template=loader.get_template('add_book.html')
   context = {'genres': genres,}

   return HttpResponse(template.render(context,request))
