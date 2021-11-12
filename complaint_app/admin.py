from django.contrib import admin
from complaint_app.models import Complaint
# Register your models here.


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('resolved', )