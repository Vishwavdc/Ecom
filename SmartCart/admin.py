from django.contrib import admin
from .models import Book ,Rating,User
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ImportData(ImportExportModelAdmin):
    pass

admin.site.register(Book,ImportData)
admin.site.register(User,ImportData)
admin.site.register(Rating,ImportData)
