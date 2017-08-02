from django.contrib import admin
from qa.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]
    search_fields = ['id']

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
