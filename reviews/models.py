from django.db import models
from django.contrib import auth
# Create your models here.
class Publisher(models.Model):
    name =  models.CharField(max_length=255,help_text="publisher's name")
    website  = models.URLField(max_length=200,help_text="publisher's website")
    email   = models.EmailField(max_length=254,help_text="publishers's email")

    def __str__(self):
        return self.name

class Contributor(models.Model):
    first_names = models.CharField(max_length=50,help_text="The contributors first names")
    last_names  = models.CharField(max_length=50,help_text="The contributors last names")
    email = models.EmailField(help_text="The contact email for the contributor")

    def __str__(self):
        return self.first_names    

class Book(models.Model):
    title  = models.CharField(max_length=50,help_text="title of the book")
    publication  = models.DateField(verbose_name="data the book was published")
    isbn = models.CharField(max_length=20,verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    contributor = models.ManyToManyField("Contributor",through="BookContributor")

    def __str__(self):
        return self.title

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True,help_text= "The date and time the review was created.")
    date_edited = models.DateTimeField(null=True, help_text= "The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book that this review is for.")    