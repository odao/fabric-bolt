from django.contrib import admin

import models


class ConfigurationModelAdmin(admin.ModelAdmin):
    list_display = ['project', 'stage', 'key', 'value']


admin.site.register(models.Project)
admin.site.register(models.ProjectType)
admin.site.register(models.Configuration, ConfigurationModelAdmin)
admin.site.register(models.Stage)