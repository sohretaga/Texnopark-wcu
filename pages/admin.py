from django.contrib import admin
from .models import Contact, News, Project

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
  list_display = ('fullname', 'number', 'email')

class NewsAdmin(admin.ModelAdmin):
  list_display = ('title', 'date')

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'finished_or_not')

admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
