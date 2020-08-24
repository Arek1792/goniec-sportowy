from django.contrib import admin
from .models import Article



class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}



# Register your models here.
admin.site.register(Article, ArticleAdmin)