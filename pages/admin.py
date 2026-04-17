from django.contrib import admin
from .models import Programme, Genre, Review


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')
    ordering = ('title',)
    search_fields = ('title', 'genre__name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('programme', 'reviewer_name', 'rating')
    ordering = ('programme', 'reviewer_name')
    search_fields = ('programme__title', 'reviewer_name')


admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)