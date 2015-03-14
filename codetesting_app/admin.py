from django.contrib import admin
from .models import *

# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
	model = Questions
	list_display = ('questions','function_name','test_function','expected_ans')
	search_fields = ['function_name']

admin.site.register(Questions, QuestionsAdmin)