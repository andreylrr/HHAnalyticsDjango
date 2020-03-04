from django.contrib import admin
from .models import Skills, Regions, Vacancies, Prof_Specs, Prof_Area

# Register your models here.
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'vac_city')

@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display=('id', 'name' )

@admin.register(Prof_Specs)
class Prof_SpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Prof_Area)
class Prof_AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
