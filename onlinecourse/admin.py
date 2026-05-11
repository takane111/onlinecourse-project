
from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# Register your models here
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

from .models import Course, Lesson, Question, Choice, Submission, Instructor, Learner # Add them to the import

# Add these registration lines at the bottom
admin.site.register(Instructor)
admin.site.register(Learner)