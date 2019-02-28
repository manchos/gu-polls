from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class ChoicesInline(admin.TabularInline):
    model = Choice




class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'pub_date',
    )
    # list_select_related = ('ice_check_post',)
    inlines = [ChoicesInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
