from django.contrib import admin

from .models import Issue, Article, Category

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Issue, IssueAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
