from django.contrib import admin
from core.models import *


# yıldız ile core içindeki her şeyi import ettik.

# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'updated_date',
                    'created_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date', ]

    class Meta:
        model = Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'department', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['school_name', 'department']
    list_editable = ['school_name', 'department', 'start_date', 'end_date', ]

    class Meta:
        model = Education


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'updated_date', 'created_date']
    search_fields = ['link', 'icon', ]
    list_editable = ['order', 'link', 'icon', ]

    class Meta:
        model = SocialMedia


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'language_name', 'level', 'updated_date', 'created_date']
    search_fields = ['language_name', 'level', ]
    list_editable = ['order', 'language_name', 'level', ]

    class Meta:
        model = Language


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ref_name', 'ref_company', 'ref_job', 'ref_number', 'updated_date', 'created_date']
    search_fields = ['ref_name', 'ref_company', 'ref_job', 'ref_number', ]
    list_editable = ['ref_name', 'ref_company', 'ref_job', 'ref_number', ]

    class Meta:
        model = Reference
