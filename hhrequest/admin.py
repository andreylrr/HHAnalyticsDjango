from django.contrib import admin
from .models import Requests

# Register your models here.
@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','region','text_request','file_name','status','created','updated')

