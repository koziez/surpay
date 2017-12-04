from django.contrib import admin

from .models import Choice, Question, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'date_made')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)
