from .models import Question, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ["choice_text"]


class QuestionAdmin(admin.ModelAdmin):
    fieldset = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    # readonly_fields = ["test_fields"]

    # description functions like a model field's verbose_name
    @admin.display(description="My readonly field")
    def test_fields(self, instance):
        # assuming get_full_address() returns a list of strings
        # for each line of the address and you want to separate each
        # line by a linebreak
        return instance.info


admin.site.register(Question, QuestionAdmin)

