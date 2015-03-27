from django.contrib import admin

# Register your models here.
from .models import Course, CourseSection, SubSection, Question, Answer

class CourseSectionAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp' #updated
    search_fields = ['title', 'description']
    list_display = ['title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = CourseSection

admin.site.register(CourseSection, CourseSectionAdmin)


admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Answer)