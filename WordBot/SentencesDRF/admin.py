
from django.contrib import admin
from .models import Question, Answer, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name_Category',
    ]

class AnswerInl(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdm(admin.ModelAdmin):
    list_display = ('question_fild',)
    inlines = [AnswerInl]
