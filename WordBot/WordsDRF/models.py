from django.db import models

class Words(models.Model):
    GENDERS = [
        ('der', 'Der'),
        ('die', 'Die'),
        ('das', 'Das'),
    ]



    word = models.CharField(verbose_name="Word", max_length=100)
    gender = models.CharField(verbose_name="Gender", max_length=3, choices=GENDERS)
    catagory = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
#   wordClass = models.CharField(verbose_name="WordClass", max_length=9, choices=WordClass)

    def __str__(self):
        return self.gender + "" + self.word

class Category(models.Model):

    nameCategory = models.CharField(verbose_name="WordClass", max_length=9, db_index=True)

    def __str__(self):
        return self.nameCategory
