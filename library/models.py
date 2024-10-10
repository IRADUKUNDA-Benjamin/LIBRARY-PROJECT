from django.db import models

# Create your models here.


class Genre(models.Model):
   name=models.CharField(max_length=50)
   def __str__(self):
      return f"{self.name}"
class Book(models.Model):
   title=models.CharField(max_length=150)
   author=models.CharField(max_length=100)
   genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
   price=models.IntegerField()
   ISBN=models.CharField(max_length=100,unique=True)
   publication_date=models.DateField()
   available_copies=models.IntegerField()

   def __str__(self):
      return self.title


class Staff(models.Model):
   name=models.CharField(max_length=100)
   mail=models.EmailField(max_length=100)
   password=models.CharField(max_length=100)
   


class Member(models.Model):
   name=models.CharField(max_length=100)
   email=models.EmailField()
   phone=models.CharField(max_length=15)
   membership_date=models.DateField()

   def __str__(self):
      return self.name

class Loan(models.Model):
   book=models.ForeignKey(Book, on_delete=models.CASCADE)
   member=models.ForeignKey(Member, on_delete=models.CASCADE)
   loan_date=models.DateField()
   return_date=models.DateField()
   created_at = models.DateField(auto_now_add=True)  # Tracks creation time
   updated_at = models.DateField(auto_now=True)      # Tracks last update time

   def __str__(self):
      return f"{self.book} borrowed by {self.member}"

