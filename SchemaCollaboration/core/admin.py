from django.contrib import admin

from .models import Schema, Person


class SchemaAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name', 'schema',)
    list_display = ('uuid', 'name', 'collaborator_names', 'created_on', 'modified_on', 'schema',)
    ordering = ('uuid',)
    readonly_fields = ('uuid', 'created_on', 'modified_on',)

    def collaborator_names(self, obj):
        names = ', '.join([collaborator.name for collaborator in obj.collaborators.all()])

        return names


class PersonAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'full_name',)
    list_display = ('uuid', 'full_name', 'created_on', 'modified_on',)
    readonly_fields = ('uuid', 'created_on', 'modified_on',)


admin.site.register(Schema, SchemaAdmin)
admin.site.register(Person, PersonAdmin)
