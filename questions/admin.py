from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('options',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Submission)

admin.site.site_header = "UPACHAR Admin Portal"
admin.site.site_title = "UPACHAR Admin Portal"
admin.site.index_title = "Welcome, UPACHAR admin"
