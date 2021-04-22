from django.contrib import admin
from .models import Store, Category, Metric
from .forms import StoreForm

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    form = StoreForm
    list_display = ("title", "author")
    list_filter = ("category",)
    search_fields = ("title",)
    readonly_fields = ("author",)


class StoreInline(admin.StackedInline):
    model = Store
    max_num = 3
    extra = 1


class TagAdmin(admin.ModelAdmin):
    inlines = [StoreInline]


admin.site.register(Store, StoreAdmin)
admin.site.register(Category)
admin.site.register(Metric, TagAdmin)
