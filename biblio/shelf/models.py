from django.db import models ##co to


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self): ##zwraca nam stringa - nazw; ustawia nazwa w bazie
        return "{first_name} {last_name}".format(first_name=self.first_name,
                                                 last_name=self.last_name)
    # formatowanie? ? ? ? ?


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)  #pole znakowe
    author = models.ForeignKey('Author')  #asocjacja ???
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey('Publisher')


# Create your models here.
