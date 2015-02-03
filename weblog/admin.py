from django.contrib import admin

from weblog.models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}

    def get_queryset(self, request):
        qs = self.model.objects.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        # see also: https://stackoverflow.com/questions/1545067/django-specify-which-model-manager-django-admin-should-use
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
