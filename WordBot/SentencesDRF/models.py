from django.db import models

""""  
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
"""




class Question(models.Model):

    question_fild = models.CharField(max_length=200)
    catagory = models.ForeignKey('Category', related_name='catagory', on_delete=models.PROTECT, null=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_fild = models.CharField(max_length=100)
    right_answer = models.BooleanField(default=False)

    def __str__(self):
        return '%s: %s %s' % (self.question, self.answer_fild, self.right_answer)


    class Meta:
        order_with_respect_to = 'question'
        unique_together = ['question', 'answer_fild']


class Category(models.Model):
    name_Category = models.CharField(verbose_name="Question_catagory", default= 'Fist_category', max_length=50, db_index=True)
