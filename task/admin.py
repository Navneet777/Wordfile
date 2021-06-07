from django.contrib import admin
from task.models import FileModel
# Register your models here.
class FileModelAdmin(admin.ModelAdmin):
    list_display = ['id','word_file']

admin.site.register(FileModel,FileModelAdmin)
