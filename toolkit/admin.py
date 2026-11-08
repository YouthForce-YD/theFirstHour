from django.contrib import admin
from .models import Situation, EvidenceStep, SupportChannel, IncidentReport


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ('titleBn', 'titleEn', 'slug', 'displayOrder', 'isActive')
    list_editable = ('displayOrder', 'isActive')
    prepopulated_fields = {'slug': ('titleEn',)}


@admin.register(EvidenceStep)
class EvidenceStepAdmin(admin.ModelAdmin):
    list_display = ('stepNumber', 'stepLabelBn', 'instructionBn', 'instructionEn')
    ordering = ('stepNumber',)


@admin.register(SupportChannel)
class SupportChannelAdmin(admin.ModelAdmin):
    list_display = ('titleBn', 'channelType', 'phoneDial', 'displayOrder', 'isActive')
    list_editable = ('displayOrder', 'isActive')
    list_filter = ('channelType', 'isActive')


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'situation', 'offenderUsername', 'requestPeerSupport', 'status', 'createdAt')
    list_filter = ('status', 'requestPeerSupport', 'situation')
    search_fields = ('user__username', 'offenderUsername', 'incidentDetails')
